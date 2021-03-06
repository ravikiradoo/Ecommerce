# Generated by Django 2.2.6 on 2020-01-04 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shipping_profile', '0001_initial'),
        ('billing_profile', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='order_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=25, null=True, unique=True)),
                ('order_status', models.CharField(choices=[('ordered', 'Ordered'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('returned', 'Returned'), ('refunded', 'Refunded')], max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('shipping', models.DecimalField(decimal_places=2, default=40.0, max_digits=10)),
                ('billing_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing_profile.Billing_Profile')),
                ('order_item', models.ManyToManyField(blank=True, null=True, to='order.order_item')),
                ('shipping_proile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shipping_profile.Shipping_Profile')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
