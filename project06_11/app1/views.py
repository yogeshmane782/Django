from django.shortcuts import render

# Create your views here.
def child1(request):
    response=render(request,"app1/child1.html")
    return response
def child2(request):
    response=render(request,"app1/child2.html")
    return response