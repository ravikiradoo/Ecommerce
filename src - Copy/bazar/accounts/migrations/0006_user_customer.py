# Generated by Django 2.2.6 on 2020-01-04 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200104_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='customer',
            field=models.BooleanField(default=False),
        ),
    ]
