from django.shortcuts import render
from app1.models import*
# Create your views here.
def home(request):
    response=render(request,"app1/index.html")
    return response
def dept_temp(request):
    response=render(request,"app1/create_dept.html")
    return response
    
def emp_temp(request):
    response=render(request,"app1/create_emp.html")
    return response
def list_emp_temp(request):
    response=render(request,"app1/list_emp.html")
    return response
def create_dept(request):
    deptno=int(request.GET['deptno'])
    dname=request.GET['dname']
    try:
        d=Dept.objects.create(deptno=deptno,dname=dname)
        d.save()
        msg="Department Added..."
    except:
        msg="Invalid deptno"
    response=render(request,"app1/create_dept.html",context={'msg':msg})
    return response
def create_emp(request):
    empno=int(request.GET['eno'])
    ename=request.GET['ename']
    job=request.GET['job']
    salary=float(request.GET['sal'])
    deptno=int(request.GET['deptno'])
    try:
        dept=Dept.objects.get(deptno=deptno)
        e=Employee.objects.create(empno=empno,ename=ename,job=job,salary=salary,dept=dept)
        e.save()
        msg="Employee Added"
    except:
        msg="Error in Adding Employee"
    response=render(request,"app1/create_emp.html",context={'msg':msg})
    return response
def display_emp(request):
    deptno=int(request.GET['deptno'])
    dept=Dept.objects.get(deptno=deptno)
    qs=Employee.objects.filter(dept=dept)
    response=render(request,"app1/list_emp.html",context={'qs':qs})
    return response
