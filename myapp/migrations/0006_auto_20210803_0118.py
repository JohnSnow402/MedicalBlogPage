# Generated by Django 3.2.5 on 2021-08-02 21:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210803_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpost',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 3, 1, 18, 55, 194382)),
        ),
        migrations.AlterField(
            model_name='addpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
