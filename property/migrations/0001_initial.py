# Generated by Django 3.0.1 on 2019-12-31 14:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import property.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Property Name', max_length=20)),
                ('description', models.TextField(blank=True, help_text='Property Description')),
                ('bedroom', models.PositiveIntegerField(help_text='No. of bedrooms', validators=[django.core.validators.MinValueValidator(1)])),
                ('bathroom', models.PositiveIntegerField(help_text='No. of bathrooms', validators=[django.core.validators.MinValueValidator(1)])),
                ('availability', models.DateField(help_text='Date from which the property is available for rent', validators=[property.models.validate_availability])),
                ('catergory', models.CharField(choices=[('apartment', 'Apartment'), ('room', 'Room'), ('bungalow', 'bungalow'), ('house', 'House')], help_text='Property Type', max_length=20)),
                ('interior', models.CharField(choices=[('unfurnished', 'Unfurnished'), ('semi-furnished', 'Semi-furnished'), ('furnished', 'furnished')], help_text='Property Type', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.DecimalField(decimal_places=2, help_text='Property rent', max_digits=6)),
                ('deposit', models.DecimalField(decimal_places=2, help_text='Property deposit', max_digits=6)),
                ('property', models.OneToOneField(default=100, help_text='Property', on_delete=django.db.models.deletion.CASCADE, related_name='property_price', to='property.Property')),
            ],
        ),
    ]
