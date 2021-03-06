# Generated by Django 3.0.1 on 2019-12-31 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Image url')),
                ('alt', models.CharField(max_length=20, verbose_name='Image description ')),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name', max_length=20)),
                ('mid_name', models.CharField(blank=True, help_text='Mid Name', max_length=10, null=True)),
                ('last_name', models.CharField(help_text='Last Name', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=128, verbose_name='Street')),
                ('locality', models.CharField(max_length=128, verbose_name='Locality')),
                ('city', models.CharField(default='Eindhoven', max_length=15, verbose_name='City')),
                ('country', models.CharField(default='Netherlands', max_length=15, verbose_name='Country')),
                ('zip_code', models.CharField(default='5611KT', max_length=12, verbose_name='Postal code')),
                ('property', models.OneToOneField(default=None, help_text='Property', on_delete=django.db.models.deletion.CASCADE, related_name='address', to='property.Property')),
            ],
        ),
    ]
