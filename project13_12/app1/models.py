from django.db import models

# Create your models here.
class Product(models.Model):
    proid=models.CharField(max_length=20,primary_key=True)
    prodname=models.CharField(max_length=20)
    qty=models.IntegerField()
    price=models.FloatField()