# Generated by Django 2.2.6 on 2020-01-04 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200104_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='staff',
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('EMPLOYEE', 'EMPLOYEE'), ('CUSTOMER', 'CUSTOMER')], default='CUSTOMER', max_length=100),
        ),
    ]