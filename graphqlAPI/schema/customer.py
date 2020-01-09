import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from customer.models import Customer
from common.models import Address


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
        address = Address(street=user_data.street,
                          city=user_data.city,
                          country=user_data.country,
                          zip_code=user_data.zip_code)
        address.save()
        customer = Customer(user=user, phone=user_data.phone,
                            address=address)

        return CreateUser(user=customer)


class CustomerMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
