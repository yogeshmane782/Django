from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)
    password=models.CharField(max_length=15)