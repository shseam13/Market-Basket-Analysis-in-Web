# Generated by Django 4.1.4 on 2022-12-29 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact_date',
            new_name='purchase_date',
        ),
    ]