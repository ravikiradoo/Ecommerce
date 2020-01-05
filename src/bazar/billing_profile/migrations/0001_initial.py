# Generated by Django 2.2.6 on 2020-01-04 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=25)),
                ('stripe_id', models.CharField(blank=True, max_length=220, null=True)),
                ('Address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='addresses.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=25, null=True, unique=True)),
                ('paid', models.BooleanField(default=False)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('payement_method', models.CharField(max_length=100)),
                ('stripe_id', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(max_length=100)),
                ('Month', models.IntegerField()),
                ('Year', models.IntegerField()),
                ('brand', models.CharField(max_length=100)),
                ('last4', models.CharField(max_length=4)),
                ('Billing_Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing_profile.Billing_Profile')),
            ],
        ),
    ]
