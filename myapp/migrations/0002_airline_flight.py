# Generated by Django 5.0.7 on 2024-07-30 15:43

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('take_off_time', models.TimeField()),
                ('landing_time', models.TimeField()),
                ('seats_number', models.IntegerField(default=0)),
                ('price', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.airline')),
            ],
        ),
    ]