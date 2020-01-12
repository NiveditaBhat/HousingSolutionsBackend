from django.core.exceptions import ValidationError
from django.db import models
from django_countries import Countries
from django_countries.fields import CountryField

from customer.models import Customer
from property.models import Property


class Name(models.Model):
    first_name = models.CharField(
        max_length=20,
        help_text="First Name"
    )
    mid_name = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        help_text="Mid Name"
    )
    last_name = models.CharField(
        max_length=15,
        help_text="Last Name"
    )


class EUCountries(Countries):
    only = [
        'AT', 'BE', 'BG', 'CY', 'CZ', 'DK', 'EE', 'ES', 'FI', 'GR', 'HR',
        'FR', 'DE', 'HU', 'IE', 'IT', 'LT', 'LU', 'LV', 'MT', 'NL', 'PT',
        'RO', 'SE', 'SI', 'SK'
    ]


class Address(models.Model):
    property = models.OneToOneField(
        Property, related_name="address", help_text="Property",
        on_delete=models.CASCADE, null=True)
    customer = models.OneToOneField(
        Customer, related_name="address", help_text="Customer",
        on_delete=models.CASCADE, null=True)
    street = models.CharField(help_text="Street", max_length=128)
    city = models.CharField(
        help_text="City", max_length=15, default="Eindhoven")
    country = CountryField(countries=EUCountries,
                           help_text="Countries in EU Union", default='NL')
    zip_code = models.CharField(
        help_text="Postal code", max_length=12, default="5611KT")

    class Meta:
        verbose_name = 'Address'


class Image(models.Model):
    property = models.ForeignKey(
        Property, related_name="Image", help_text="Property Images",
        on_delete=models.CASCADE, null=True)

    url = models.URLField("url", max_length=200)
    alt = models.CharField("alt", max_length=20)

    class Meta:
        verbose_name = 'Property Image'

    def clean(self):
        total_images = Image.objects.filter(property=self.property).count()
        if(total_images > 10):
            raise ValidationError(
                "The total number of images for a property cannot exceed 10")
