from django.shortcuts import render
from app1.models import Users
# Create your views here.
def register_view(request):
    name=request.GET['fname']
    uname=request.GET['uname']
    password=request.GET['pwd']
    user=Users(name=name,uname=uname,password=password)
    user.save()
    response=render(request,"app1/register.html",context={'msg':'User Registered...'})
    return response

def signup(request):
    response=render(request,"app1/register.html")
    return response
