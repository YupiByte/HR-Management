# Generated by Django 4.2.7 on 2023-11-29 23:48

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='PR'),
        ),
    ]
