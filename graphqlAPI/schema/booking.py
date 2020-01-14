import graphene
from graphene_django import DjangoObjectType

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
        if info.context.user.is_authenticated:
            property = Property.objects.get(id=booking_data.property_id)
            booking = Booking(property=property,
                            message=booking_data.booking_message)
            booking.save()
            customer = Customer.objects.get(id=booking_data.customer_id)
            customer.booking = booking
            customer.save()
            return CreateBooking(booking=booking)


class BookingMutation(graphene.ObjectType):
    create_booking = CreateBooking.Field()
