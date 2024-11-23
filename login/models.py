from django.db import models

# Create your models here.
from django.db import models
from django import forms


class value_db(models.Model):
    mail = models.EmailField(max_length=200,default="default@example.com", unique=True)
    # mail = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    # national_ID = models.CharField(max_length=14)
    phone = models.CharField(max_length=11)
    approval = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.mail} , {self.full_name}"