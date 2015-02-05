# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    login_date = models.DateTimeField('date login_date') # date 타입에 컬럼명 login_date
    def __str__(self):
        return self.name

    def was_login(self):
        return True
    was_login.admin_order_field = 'login_date'
    was_login.boolean = True
    was_login.short_description = 'Published recently?'

    @staticmethod
    def hello_user():
        return "유저 모델 테스트 ㅋㅋ"

class Payment(models.Model):
    user = models.ForeignKey(User)
    price = models.IntegerField(default=0)

