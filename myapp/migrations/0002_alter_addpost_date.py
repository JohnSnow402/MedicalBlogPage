# Generated by Django 3.2.5 on 2021-08-02 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpost',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 2, 19, 11, 4, 594626)),
        ),
    ]
