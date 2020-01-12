import graphene
from graphene_django import DjangoObjectType

from booking.models import Booking
from property.models import Property
from customer.models import Customer


class BookingInput(graphene.InputObjectType):
    customer_id = graphene.String(required=True)
    property_id = graphene.String(required=True)


class BookingType(DjangoObjectType):
    class Meta:
        model = Booking


class CreateBooking(graphene.Mutation):
    booking = graphene.Field(BookingType)

    class Arguments:
        booking_data = BookingInput(required=True)
    
    def mutate(self, info, booking_data):
        customer = Customer.objects.get(id=booking_data.customer_id)
        property = Property.objects.get(id=booking_data.property_id)
        booking = Booking(customer=customer,
                          property=property)
        booking.save()
        return CreateBooking(booking=booking)


class BookingMutation(graphene.ObjectType):
    create_booking = CreateBooking.Field()

