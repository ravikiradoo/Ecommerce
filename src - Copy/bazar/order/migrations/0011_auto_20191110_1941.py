# Generated by Django 2.2.6 on 2019-11-10 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing_profile', '0001_initial'),
        ('shipping_profile', '0001_initial'),
        ('order', '0010_auto_20191108_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='billing_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing_profile.Billing_Profile'),
        ),
        migrations.AddField(
            model_name='orders',
            name='shipping_proile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shipping_profile.Shipping_Profile'),
        ),
    ]
