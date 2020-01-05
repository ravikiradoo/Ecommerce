# Generated by Django 2.2.6 on 2019-11-24 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing_profile', '0004_auto_20191124_1521'),
    ]

    operations = [
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