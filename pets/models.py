from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

import os


def get_image_path(instance, filename):
    return os.path.join('pets/static/images', str(instance.id), filename)

class Dog(models.Model):
    objects = models.Manager()
    id = models.IntegerField(primary_key = True,blank=False, null=False, default=' ')
    name = models.CharField(max_length=20, blank=True, null=True,default=' ')
    breed = models.CharField(max_length=20, blank=True, null=True,default=' ')
    color = models.CharField(max_length=20, blank=True, null=True,default=' ')
    age = models.IntegerField(default=' ')
    gender = models.CharField(max_length=10, default='')
    size = models.CharField(max_length=15, default='')
    weight = models.CharField(max_length=15, default='')
    adoption_fee = models.CharField(max_length=15, default='')
    description = models.CharField(max_length=150, default=' ')
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.name)

class Cat(models.Model):
    objects = models.Manager()
    id = models.IntegerField(primary_key = True,blank=False, null=False, default=' ')
    name = models.CharField(max_length=20, blank=True, null=True,default=' ')
    breed = models.CharField(max_length=20, blank=True, null=True, default=' ')
    color = models.CharField(max_length=20, blank=True, null=True, default=' ')
    age = models.IntegerField(default=' ')
    gender = models.CharField(max_length=10, default='')
    size = models.CharField(max_length=15, default='')
    weight = models.CharField(max_length=15, default='')
    adoption_fee = models.CharField(max_length=15, default='')
    description = models.CharField(max_length=150, default=' ')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

