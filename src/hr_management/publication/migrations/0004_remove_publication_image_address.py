# Generated by Django 4.2.6 on 2023-11-03 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0003_alter_publication_image_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='image_address',
        ),
    ]
