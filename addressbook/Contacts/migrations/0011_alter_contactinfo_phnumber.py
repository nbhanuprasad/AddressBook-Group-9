# Generated by Django 3.2.8 on 2021-10-21 22:09

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Contacts', '0010_auto_20211021_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='phnumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Primary Phone Number'),
        ),
    ]
