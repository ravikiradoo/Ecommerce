# Generated by Django 2.2.6 on 2020-01-05 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('billing_profile', '0002_auto_20200105_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing_profile',
            name='Email',
        ),
        migrations.AddField(
            model_name='billing_profile',
            name='Address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='addresses.Address'),
        ),
    ]
