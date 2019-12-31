from django.db import models
from django.core.validators import MinValueValidator
from datetime import date
from django.core.exceptions import ValidationError
from common.models import Address, Image


def validate_availability(value):
    today = date.today()
    if value < today:
        raise ValidationError(
            'Property Availability cannot be set to the past date.')


class PropertyPrice(models.Model):
    rent = models.DecimalField(
        help_text="Property rent", max_digits=6, decimal_places=2)
    deposit = models.DecimalField(
        help_text="Property deposit", max_digits=6, decimal_places=2)


class PropertyImages(models.Model):
    image = models.ForeignKey(Image, related_name='+',
                              on_delete=models.CASCADE)


class Property(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Property Name"
    )
    description = models.TextField(
        blank=True,
        help_text="Property Description"
    )
    bedroom = models.PositiveIntegerField(
        help_text="No. of bedrooms", validators=[MinValueValidator(1)])
    bathroom = models.PositiveIntegerField(
        help_text="No. of bathrooms", validators=[MinValueValidator(1)])
    availability = models.DateField(
        help_text="Date from which the property is available for rent", validators=[validate_availability])
    catergory = models.CharField(
        max_length=20,
        help_text="Property Type",
        choices=(
            ("apartment", "Apartment"),
            ("room", "Room"),
            ("bungalow", "bungalow"),
            ("house", "House")
        )
    )
    interior = models.CharField(
        max_length=20,
        help_text="Property Type",
        choices=(
            ("unfurnished", "Unfurnished"),
            ("semi-furnished", "Semi-furnished"),
            ("furnished", "furnished")
        )
    )
    price = models.OneToOneField(
        PropertyPrice, related_name="+", help_text="Property Price", on_delete=models.CASCADE)

    address = models.OneToOneField(
        Address, related_name="+", help_text="Property Address", on_delete=models.CASCADE)

    property_images = models.OneToOneField(
        PropertyImages, related_name="+", help_text="Property Images", on_delete=models.CASCADE)
