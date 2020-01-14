from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneField(blank=True, null=True, help_text='Phone number')
    
    class Meta:
        verbose_name_plural = 'Customers registered under HousingSolutions'

    def __str__(self):
        return "Customer {id} : {user}".format(id=self.id,
                                               user=self.user.username)
