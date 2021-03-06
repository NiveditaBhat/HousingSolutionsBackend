# Generated by Django 3.0.2 on 2020-01-14 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0009_auto_20200105_1014'),
        ('booking', '0003_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, help_text='Booking message', null=True)),
                ('property', models.OneToOneField(help_text='Property', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='property.Property')),
            ],
            options={
                'verbose_name_plural': 'Bookings for properties',
            },
        ),
    ]
