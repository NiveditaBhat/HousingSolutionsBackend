import graphene
from graphene_django.types import DjangoObjectType

from property.models import Property, PropertyPrice
from common.models import Address, Image


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


class PropertyQuery(graphene.ObjectType):
    all_properties = graphene.List(PropertyType)

    def resolve_all_properties(self, info, **kwargs):
        return Property.objects.all()
