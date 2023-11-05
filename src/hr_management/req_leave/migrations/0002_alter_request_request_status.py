# Generated by Django 4.2.6 on 2023-11-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('req_leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending', max_length=8),
        ),
    ]
