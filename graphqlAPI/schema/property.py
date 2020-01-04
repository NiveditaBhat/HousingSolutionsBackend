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


class PropertyQuery(graphene.ObjectType):
    all_properties = graphene.List(PropertyType)
    search_properties = graphene.List(
        PropertyType, params=SearchInput())

    def resolve_all_properties(self, info, **kwargs):
        return Property.objects.all()

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