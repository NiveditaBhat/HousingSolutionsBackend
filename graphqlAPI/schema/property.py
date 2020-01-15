
import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from common.models import Address, Image
from property.models import Property, PropertyPrice


def sort_properties(results, param, order):
    """
    Sort properties by parameters - availability or price
    order - ascending or descending
    """
    if param:
        if order == 2:
            param = '-'+param

        return results.order_by(param)


class PropertyPrice(DjangoObjectType):
    class Meta:
        model = PropertyPrice


class PropertyImage(DjangoObjectType):
    class Meta:
        model = Image


class PropertyAddress(DjangoObjectType):
    class Meta:
        model = Address


class PropertyType(DjangoObjectType):
    class Meta:
        model = Property


class SearchInput(graphene.InputObjectType):
    interior = graphene.String(required=False)
    bedroom = graphene.Int(required=False)
    city = graphene.String(required=False)
    country = graphene.String(required=False)
    rent = graphene.Float(required=False)
    category = graphene.String(required=False)


class SortByFields(graphene.Enum):
    price = "property_price__rent"
    availability = "availability"


class SortOrder(graphene.Enum):
    ASC = 1
    DSC = 2


class PropertyQuery(graphene.ObjectType):
    all_properties = graphene.List(PropertyType)
    property = graphene.Field(PropertyType, property_id=graphene.String())
    search_properties = graphene.List(
        PropertyType, filter_params=SearchInput(),
        sort_params=SortByFields(),
        order=SortOrder())

    def resolve_all_properties(self, info, **kwargs):
        try:
            return Property.objects.all()
        except Property.DoesNotExist:
            return None

    def resolve_property(self, info, property_id):
        try:
            return Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            raise GraphQLError('Unable to retrive property with id {id}'.format(id=property_id))

    def resolve_search_properties(self, info, filter_params=None,
                                  sort_params="availability",
                                  order=1, **kwargs):
        """
        Search properties by parameters - interior, bedroom, price, city,
        country and rent
        Sort by price or availability
        """     
        if filter_params:
            query = {"interior": Q(interior__iexact=filter_params.interior),
                        "bedroom": Q(bedroom__icontains=filter_params.bedroom),
                        "city": Q(address__city__iexact=filter_params.city),
                        "country": Q(address__country__iexact=filter_params.country),
                        "rent": Q(property_price__rent__lte=filter_params.rent),
                        "category": Q(category__iexact=filter_params.category)
                        }

            filter = ()
            for k, v in query.items():
                if k in filter_params:
                    if len(filter) == 0:
                        filter = v
                    else:
                        filter = v & filter

            search_results = Property.objects.filter(filter)
            sorted_results = sort_properties(
                search_results, sort_params, order)
            return sorted_results

        return Property.objects.all()
