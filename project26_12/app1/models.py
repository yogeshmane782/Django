from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    password2=models.CharField(max_length=20)