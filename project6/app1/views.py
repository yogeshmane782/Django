from django.shortcuts import render

# Create your views here.
def home(request):
    response=render(request,"app1/index.html")
    return response
def adding_num(request):
    num1=int(request.GET['n1'])
    num2=int(request.GET['n2'])
    num3=num1+num2
    response=render(request,"app1/result.html",context={'res':num3})
    return response
