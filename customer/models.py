from django.db import models
from phone_field import PhoneField


class Customer(models.Model):
    email = models.EmailField(max_length=254, help_text='Email Id')
    phone = PhoneField(blank=True, null=True, help_text='Phone number')

    class Meta:
        verbose_name_plural = 'Customers registered under HousingSolutions'

    def __str__(self):
        return "Customer {id}".format(id=self.id)
