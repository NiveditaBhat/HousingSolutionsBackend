from graphene import Field, ObjectType, Schema

from .property import PropertyQuery
from .customer import CustomerMutation


def resolve_self(_, info):
    """
    Generic resolver used for namespacing the schemas.
    """
    return info.return_type.graphene_type()


class Query(ObjectType):
    """
    Root query which includes all queries from other modules
    """
    property = Field(PropertyQuery, resolver=resolve_self)


class Mutation(ObjectType):
    """
    Root mutation which includes all mutations from other modules
    """
    customer = Field(CustomerMutation, resolver=resolve_self)


schema = Schema(query=Query, mutation=Mutation)
