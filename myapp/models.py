from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE
# Create your models here.


class AddPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    date = models.DateField(default=datetime.now(), blank=True)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    sub_body = models.TextField(null=True, blank=True)
    date = models.DateField(default=datetime.now(), blank=True)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title


class AddComment(models.Model):
    post = models.ForeignKey(
        AddPost, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    name = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now(), blank=True)

    def __str__(self):
        return f'{self.name} added {self.body} to {self.post} on: {self.date}'
