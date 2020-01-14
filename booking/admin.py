from django.contrib import admin

from .models import Booking
from customer.models import Customer



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    readonly_fields = ['message']
   
