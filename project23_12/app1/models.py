from django.db import models

# Create your models here.
class User(models.Model):
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    username=models.CharField()
    password=models.CharField()