# Generated by Django 3.0.1 on 2019-12-31 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyprice',
            name='deposit',
            field=models.DecimalField(decimal_places=2, default=100, help_text='Property deposit (in Euros)', max_digits=6),
        ),
        migrations.AlterField(
            model_name='propertyprice',
            name='rent',
            field=models.DecimalField(decimal_places=2, default=100, help_text='Property rent (in Euros)', max_digits=6),
        ),
    ]
