# Generated by Django 4.1.4 on 2022-12-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_catagory_product_min_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=490),
            preserve_default=False,
        ),
    ]