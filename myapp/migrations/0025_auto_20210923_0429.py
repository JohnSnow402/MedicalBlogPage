# Generated by Django 3.2.5 on 2021-09-23 00:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20210824_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcomment',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 23, 4, 29, 28, 992006)),
        ),
        migrations.AlterField(
            model_name='addpost',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 23, 4, 29, 28, 992006)),
        ),
        migrations.AlterField(
            model_name='services',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 23, 4, 29, 28, 992006)),
        ),
    ]
