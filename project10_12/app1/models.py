from django.db import models

# Create your models here.
class App1Product(models.Model):
    proid = models.CharField(primary_key=True, max_length=20)
    prodname = models.CharField(max_length=20)
    qty = models.IntegerField()
    price = models.FloatField()
    class Meta:
        managed = False
        db_table = 'app1_product'