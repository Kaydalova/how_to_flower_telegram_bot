# Generated by Django 2.2.16 on 2023-04-04 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0009_auto_20230401_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.TimeField(default=datetime.datetime.now, verbose_name='Время оповещения'),
        ),
    ]
