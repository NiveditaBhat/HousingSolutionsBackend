from django.db import models

from customer.models import Customer
from property.models import Property


class Booking(models.Model):
    property = models.ForeignKey(
        Property, related_name="booking", help_text="Property",
        on_delete=models.CASCADE, null=True)
    customer = models.OneToOneField(
        Customer, related_name="booking", help_text="Customer",
        on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Bookings for properties'

    def __str__(self):
        return "Booking {id} : {name}".format(name=self.property.name,
                                              id=self.id)
