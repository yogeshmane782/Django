from django.shortcuts import render

# Create your views here.
def home(request):
    response=render(request,"app1/index.html")
    return response
def add(request):
    n1=eval(request.GET['num1'])
    n2=eval(request.GET['num2'])
    n3=n1+n2
    response=render(request,"app1/add.html",context={'n1':n1,'n2':n2,'n3':n3})
    return response