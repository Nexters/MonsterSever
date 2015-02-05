# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    def __str__(self):
        return self.name

    @staticmethod
    def hello_user():
        return "가 나 다 라 a b c d"
