# Generated by Django 2.2.6 on 2020-01-05 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing_profile', '0003_auto_20200105_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='Billing_Profile',
            new_name='user',
        ),
    ]
