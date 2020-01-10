import graphene
import graphql_jwt
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from common.models import Address
from customer.models import Customer


class CustomerInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    phone = graphene.String(required=True)
    street = graphene.String(required=True)
    city = graphene.String(required=True)
    country = graphene.String(required=True)
    zip_code = graphene.String(required=True)


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer


class CreateUser(graphene.Mutation):
    user = graphene.Field(CustomerType)

    class Arguments:
        user_data = CustomerInput(required=True)
        
    def mutate(self, info, user_data):
        user = get_user_model()(username=user_data.username,
                                email=user_data.email, 
                                first_name=user_data.first_name,
                                last_name=user_data.last_name)
        user.set_password(user_data.password)
        user.save()
        customer = Customer(user=user, phone=user_data.phone)
        customer.save()
        address = Address(customer=customer, 
                          street=user_data.street,
                          city=user_data.city,
                          country=user_data.country,
                          zip_code=user_data.zip_code)
        address.save()

        return CreateUser(user=customer)


class CustomerMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class CustomerQuery(graphene.ObjectType):
    customer = graphene.Field(CustomerType)

    def resolve_customer(self, info):
        if info.context.user.is_authenticated:
            return Customer.objects.get(user=info.context.user)
        return None


