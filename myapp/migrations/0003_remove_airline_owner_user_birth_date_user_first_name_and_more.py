# Generated by Django 5.0.7 on 2024-07-31 03:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_airline_flight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airline',
            name='owner',
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.date(2024, 7, 31)),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='amir', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='male', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='moradi', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='national_id_number',
            field=models.CharField(default='0150227922', max_length=50),
        ),
    ]
