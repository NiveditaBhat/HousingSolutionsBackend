import graphene
from graphene_django.types import DjangoObjectType

from property.models import Property, PropertyPrice
from common.models import Address, Image
from django.db.models import Q


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
        PropertyType, params=SearchInput())
    sort_properties = graphene.List(
        PropertyType, param=SortByFields(), order=SortOrder())

    def resolve_all_properties(self, info, **kwargs):
        return Property.objects.all()

    def resolve_property(self, info, property_id):
        return Property.objects.get(id=property_id)

    def resolve_search_properties(self, info, params=None, **kwargs):
        """
        Search properties by parameters - interior, bedroom, price, city, 
        country and rent
        """
        if params:
            query = {"interior": Q(interior__iexact=params.interior),
                     "bedroom": Q(bedroom__icontains=params.bedroom),
                     "city": Q(address__city__iexact=params.city),
                     "country": Q(address__country__iexact=params.country),
                     "rent": Q(property_price__rent__lte=params.rent)
                     }
            filter = ()
            for k, v in query.items():
                if k in params:
                    if len(filter) == 0:
                        filter = v
                    else:
                        filter = v & filter
            return Property.objects.filter(filter)

        return Property.objects.all()

    def resolve_sort_properties(self, info, param="availability", order=1, **kwargs):
        """
        Sort properties by parameters - availability or price
        order - ascending or descending
        """
        if param:
            if order == 2:
                param = '-'+param
            return Property.objects.all().order_by(param)
