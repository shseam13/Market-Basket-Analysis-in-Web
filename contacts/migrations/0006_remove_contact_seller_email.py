# Generated by Django 4.1.4 on 2022-12-29 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_contact_seller_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='seller_email',
        ),
    ]
