from django.contrib import admin
from django.utils.html import mark_safe

from common.models import Address, Image
from property.models import Property, PropertyPrice


class AddressInline(admin.StackedInline):
    model = Address
    fields = ['street', 'city', 'country', 'zip_code']


class PropertyPriceInline(admin.StackedInline):
    model = PropertyPrice


class ImageInline(admin.StackedInline):
    model = Image
    readonly_fields = ["image_tag"]

    def image_tag(self, obj):
        return mark_safe('<img src="{url}" width="200" height="300" />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
        )

    image_tag.short_description = 'Preview'
    image_tag.allow_tags = True


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [AddressInline, PropertyPriceInline, ImageInline]
