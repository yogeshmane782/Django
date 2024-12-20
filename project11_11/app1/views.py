from django.shortcuts import render
import datetime
# Create your views here.
def show_employee(request):
    emp_data={101:['naresh',datetime.date(2020,8,12)],
              102:['suresh',datetime.date(2021,9,10)],
              103:['ramesh',datetime.date(2020,11,15)],
              104:['suresh',datetime.date(2020,11,15)]
              }
    response=render(request,"app1/show_emp.html",context={'emp_data':emp_data})
    return response