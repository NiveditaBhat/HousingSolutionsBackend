from django.db import models
from phone_field import PhoneField


class Customer(models.Model):
    email = models.EmailField(max_length=254, help_text='Email Id')
    phone = PhoneField(blank=True, null=True, help_text='Phone number')

    def __str__(self):
        return self.name
