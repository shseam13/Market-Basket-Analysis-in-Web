# Generated by Django 4.1.4 on 2023-01-19 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_remove_contact_seller_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='messages',
            new_name='address',
        ),
    ]
