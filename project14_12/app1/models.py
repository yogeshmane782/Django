from django.db import models

# Create your models here.
class Employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=20)
    job=models.CharField(max_length=15)
    salary=models.FloatField()
    class Meta:
        db_table='app1_employee'