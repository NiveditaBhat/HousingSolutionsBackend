from django.contrib import admin

from common.models import Address

from .models import Customer
from booking.models import Booking


class BookingInline(admin.StackedInline):
    model = Booking


class AddressInline(admin.StackedInline):
    model = Address
    fields = ['street', 'city', 'country', 'zip_code']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [BookingInline, AddressInline]
