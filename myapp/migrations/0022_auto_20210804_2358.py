# Generated by Django 3.2.5 on 2021-08-04 19:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20210804_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpost',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 8, 4, 23, 58, 57, 649765)),
        ),
        migrations.CreateModel(
            name='AddComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, default=datetime.datetime(2021, 8, 4, 23, 58, 57, 649765))),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myapp.addpost')),
            ],
        ),
    ]
