# Generated by Django 2.2.6 on 2020-01-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('account_type', models.CharField(choices=[('ADMIN', 'ADMIN'), ('EMPLOYEE', 'EMPLOYEE'), ('CUSTOMER', 'CUSTOMER')], default='CUSTOMER', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
