# Generated by Django 3.2.5 on 2021-08-03 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_addpost_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpost',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 3, 17, 27, 46, 42018)),
        ),
    ]
