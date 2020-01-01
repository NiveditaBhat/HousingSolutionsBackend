from django.contrib import admin
from common.models import Address, Name
from .models import Customer


class AddressInline(admin.StackedInline):
    model = Address
    fields = ['street', 'city', 'country', 'zip_code']


class NameInline(admin.StackedInline):
    model = Name


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [NameInline, AddressInline]
