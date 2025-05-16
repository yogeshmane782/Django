from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=20)
    emp_salary=models.FloatField()