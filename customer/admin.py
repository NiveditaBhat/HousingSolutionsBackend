from django.contrib import admin

from common.models import Address

from .models import Customer


class AddressInline(admin.StackedInline):
    model = Address
    fields = ['street', 'city', 'country', 'zip_code']



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [AddressInline]
