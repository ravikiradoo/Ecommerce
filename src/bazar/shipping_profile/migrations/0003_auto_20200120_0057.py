# Generated by Django 2.2.6 on 2020-01-19 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_profile', '0002_remove_shipping_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping_profile',
            name='Address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='addresses.Address'),
        ),
    ]