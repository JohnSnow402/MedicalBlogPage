# Generated by Django 3.2.5 on 2021-08-24 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_auto_20210824_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addpost',
            name='sub_body',
        ),
        migrations.AlterField(
            model_name='addcomment',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 24, 21, 18, 28, 15969)),
        ),
        migrations.AlterField(
            model_name='addpost',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 24, 21, 18, 28, 15969)),
        ),
        migrations.AlterField(
            model_name='services',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 24, 21, 18, 28, 15969)),
        ),
    ]
