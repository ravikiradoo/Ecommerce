# Generated by Django 2.2.6 on 2019-11-08 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20191106_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product'),
        ),
    ]
