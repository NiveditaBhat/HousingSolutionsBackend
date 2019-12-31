from django.db import models

# Create your models here.


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


class Address(models.Model):
    street = models.CharField("Street", max_length=128)
    locality = models.CharField("Locality", max_length=128)
    city = models.CharField("City", max_length=15, default="Eindhoven")
    country = models.CharField("Country", max_length=15, default="Netherlands")
    zip_code = models.CharField("Postal code", max_length=12, default="5611KT")


class Image(models.Model):
    url = models.URLField("Image url", max_length=200)
    alt = models.CharField("Image description ", max_length=20)
