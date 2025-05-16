from django.shortcuts import render
from .models import Employee

# Create your views here.
def home(request):
    return render(request,"app1/home.html")
def add_temp(request):
    return render(request,"app1/add_emp.html")
def add_emp(request):
    emp_id=request.GET['emp_id']
    name=request.GET['name']
    salary=request.GET['salary']
    employee=Employee(emp_id=emp_id,emp_name=name,emp_salary=salary)
    employee.save()
    return render(request,"app1/add_emp.html",context={'msg':"Employee Added..."})
def update_temp(request):
    return render(request,"app1/update.html")
def update_view(request):
    emp_id=request.GET['emp_id']
    salary=request.GET['salary']
    try:
       e=Employee.objects.get(emp_id=emp_id) 
       e.emp_salary=salary 
       e.save()
       response=render(request,"app1/update.html",context={'msg':"salary updated..."})
       return response 
    except:
        response=render(request,"app1/update.html",context={'msg':'invalid Employee Id'})
        return response
def list_view(request):
    employees=Employee.objects.all()
    return render(request,"app1/list.html",context={'employees':employees})
def delete_temp(request):
    return render(request,"app1/delete.html")
def delete_view(request):
    id=request.GET['id']
    e=Employee.objects.get(emp_id=id)
    e.delete()
    return render(request,"app1/delete.html",context={'msg':"Employee Deleted..."})