# Generated by Django 2.2.6 on 2019-11-04 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20191105_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True),
        ),
    ]
