# Generated by Django 3.2.5 on 2021-08-02 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_addpost_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='addpost',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='addpost',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 3, 0, 32, 20, 868841)),
        ),
    ]
