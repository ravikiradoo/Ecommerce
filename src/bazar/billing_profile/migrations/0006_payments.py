# Generated by Django 2.2.6 on 2019-11-30 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_profile', '0005_card'),
    ]

    operations = [
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
    ]