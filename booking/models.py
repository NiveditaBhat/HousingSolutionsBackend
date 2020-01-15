from django.db import models

from property.models import Property
from customer.models import Customer


class Booking(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True,
                                 on_delete=models.CASCADE,
                                 help_text='customer')
    property = models.OneToOneField(
        Property, related_name="booking", help_text="Property",
        on_delete=models.CASCADE, null=True)
    message = models.TextField(blank=True, null=True, 
                               help_text='Booking message')

    class Meta:
        verbose_name_plural = 'Bookings for properties'

    def __str__(self):
        return "Booking {id} : {name}".format(name=self.property.name,
                                              id=self.id)
