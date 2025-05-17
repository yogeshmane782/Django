from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=models.EmailField()
    phone=models.IntegerField(max_length=10)
    password=models.CharField(max_length=8)

