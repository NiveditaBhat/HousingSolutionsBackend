import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from booking.models import Booking
from customer.models import Customer
from property.models import Property


class BookingInput(graphene.InputObjectType):
    customer_id = graphene.String(required=True)
    property_id = graphene.String(required=True)
    booking_message = graphene.String()


class BookingType(DjangoObjectType):
    class Meta:
        model = Booking


class CreateBooking(graphene.Mutation):
    booking = graphene.Field(BookingType)

    class Arguments:
        booking_data = BookingInput(required=True)
    
    def mutate(self, info, booking_data):
        if info.context.user.is_anonymous:
            raise GraphQLError('User not authenticated')
        customer = Customer.objects.get(id=booking_data.customer_id)
        property = Property.objects.get(id=booking_data.property_id)
        booking = Booking(property=property, customer=customer,
                          message=booking_data.booking_message)
        booking.save()
        return CreateBooking(booking=booking)

    
class CancelBooking(graphene.Mutation):
    booking = graphene.Field(BookingType)

    class Arguments:
        booking_id = graphene.String(required=True)
        customer_id = graphene.String(required=True)
    
    def mutate(self, info, booking_id, customer_id):
        if info.context.user.is_anonymous:
            raise GraphQLError('User not authenticated')
        customer = Customer.objects.get(id=customer_id)
        booking = Booking.objects.get(id=booking_id,
                                      customer=customer)
        booking.delete()
        return CancelBooking(booking=booking)


class BookingMutation(graphene.ObjectType):
    create_booking = CreateBooking.Field()
    cancel_booking = CancelBooking.Field()
