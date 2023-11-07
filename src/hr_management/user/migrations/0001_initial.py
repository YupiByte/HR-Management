# Generated by Django 4.2.7 on 2023-11-07 01:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('employee_type', models.CharField(max_length=30)),
                ('available_pto', models.PositiveIntegerField(default=15)),
                ('available_sickdays', models.PositiveIntegerField(default=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]