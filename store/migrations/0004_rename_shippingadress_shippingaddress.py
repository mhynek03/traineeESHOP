# Generated by Django 5.0.6 on 2024-06-27 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_category_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShippingAdress',
            new_name='ShippingAddress',
        ),
    ]
