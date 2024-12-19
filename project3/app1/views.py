from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greet1(request):
    msg="<h1>Hello Welcome</h1>"
    response=HttpResponse(msg)
    return response
def greet2(request,name):
    msg=f'<h1>Hello {name} Welcome</h1>'
    response=HttpResponse(msg)
    return response
def add(request,n1,n2):
    n3=int(n1)+int(n2)
    output=f'<h1> Sum of {n1} and {n2} is {n3}</h1>'
    response=HttpResponse(output)
    return response
def sub(request,n1,n2):
    n3=n1-n2
    output=f'Difference of {n1} and {n2} is {n3}'
    response=HttpResponse(output)
    return response