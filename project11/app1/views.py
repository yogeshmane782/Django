from django.shortcuts import render
from .models import User
from django.db.models import Q

# Create your views here.
def signup_temp(request):
    return render(request,"app1/signup.html")
def signup(request):
    name=request.GET['name']
    lname=request.GET['lname']
    email=request.GET['email']
    phone=request.GET['phone']
    password=request.GET['pwd']
    u=User(name=name,last_name=lname,email=email,phone=phone,password=password)
    u.save()
    return render(request,"app1/signup.html",context={'msg':"Register Successfully..."})
def signin_temp(request):
    return render(request,"app1/signin.html")
def signin(request):
    email=request.GET['email']
    password=request.GET['pwd']
    qs=User.objects.filter(Q(email=email) & Q(password=password))
    if len(qs)==0:
        return render(request,"app1/signin.html",context={'msg':"Invalid username and password"})
    else:
        return render(request,"app1/welcome.html",context={'email':email})