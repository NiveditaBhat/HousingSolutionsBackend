from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


def validate_availability(value):
    today = date.today()
    if value < today:
        raise ValidationError(
            'Property Availability cannot be set to the past date.')


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
        help_text="Date from which the property is available for rent",
        validators=[validate_availability])
    category = models.CharField(
        max_length=20,
        help_text="Property Type",
        choices=(
            ("apartment", "Apartment"),
            ("room", "Room"),
            ("bungalow", "Bungalow"),
            ("house", "House")
        ),
        default="apartment"
    )
    interior = models.CharField(
        max_length=20,
        help_text="Property Interior",
        choices=(
            ("unfurnished", "Unfurnished"),
            ("semi-furnished", "Semi-furnished"),
            ("furnished", "Furnished")
        ),
        default='unfurnished'
    )

    class Meta:
        verbose_name_plural = 'Properties under HousingSolutions'

    def __str__(self):
        return self.name


class PropertyPrice(models.Model):
    property = models.OneToOneField(
        Property, related_name="property_price", help_text="Property",
        on_delete=models.CASCADE, default=None)
    rent = models.DecimalField(
        help_text="Property rent (in €)", max_digits=6, decimal_places=2,
        default=00.00)
    deposit = models.DecimalField(
        help_text="Property deposit (in €)", max_digits=6, decimal_places=2,
        default=00.00)
