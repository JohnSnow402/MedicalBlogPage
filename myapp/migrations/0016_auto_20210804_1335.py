# Generated by Django 3.2.5 on 2021-08-04 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_addpost_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateField(blank=True, default=datetime.datetime(2021, 8, 4, 13, 35, 45, 444308))),
            ],
        ),
        migrations.AlterField(
            model_name='addpost',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 4, 13, 35, 45, 443307)),
        ),
    ]
