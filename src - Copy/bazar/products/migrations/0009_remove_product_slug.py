# Generated by Django 2.2.6 on 2019-10-31 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]