# Generated by Django 2.2.6 on 2019-11-08 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_order_item_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_item',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product'),
        ),
    ]
