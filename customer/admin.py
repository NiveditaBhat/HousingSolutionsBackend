from django.contrib import admin

from common.models import Address

from .models import Customer
from booking.models import Booking


class BookingInline(admin.StackedInline):
    model = Booking
    readonly_fields = ['message']


class AddressInline(admin.StackedInline):
    model = Address
    exclude = ['property']
    readonly_fields = ['street', 'city', 'country', 'zip_code']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ['phone']
    inlines = [AddressInline, BookingInline]
