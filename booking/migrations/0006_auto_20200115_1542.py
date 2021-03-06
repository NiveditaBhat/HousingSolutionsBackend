# Generated by Django 3.0.2 on 2020-01-15 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_remove_customer_booking'),
        ('booking', '0005_booking_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(blank=True, help_text='customer', null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer'),
        ),
    ]
