# Generated by Django 3.2.5 on 2021-08-02 21:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210803_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpost',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='addpost',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 3, 1, 28, 28, 820977)),
        ),
        migrations.AlterField(
            model_name='addpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='addpost',
            name='sub_body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
