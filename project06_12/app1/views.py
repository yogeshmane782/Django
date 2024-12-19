from django.shortcuts import render
from app1.forms import EmployeeForm
from app1.models import Employee
# Create your views here.
def home(request):
    response=render(request,"app1/addemp_temp.html")
    return response
def addemp_view(request):
    if request.method=="GET":
        emp_form=EmployeeForm()
        response=render(request,"app1/addemp_temp.html",context={'emp_form':emp_form})
        return response
    elif request.method=="POST":
        emp_form=EmployeeForm(request.POST)
        if emp_form.is_valid():
            emp_form.save(commit=True)
            emp_form=EmployeeForm()
            response=render(request,"app1/addemp_temp.html",context={'emp_form':emp_form,'msg':"EmployeeAddedd"})
            return response
        else:
            response=render(request,"app1/addemp_temp.html",context={'emp_form':emp_form})
            return response
def employee_view(request):
    data=Employee.objects.all()
    response=render(request,"app1/emplist_temp.html",context={'data':data})
    return response