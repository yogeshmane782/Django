from django.shortcuts import render
import datetime
# Create your views here.
def filter_test(request):
    num=45
    response=render(request,"app1/filter_test.html",context={'num':num})
    return response
def filter_test1(request):
    names=["naresh","kishore","rajesh"]
    response=render(request,"app1/filter_test1.html",context={'names':names})
    return response
def filter_test2(request):
    dt=datetime.datetime.today()
    response=render(request,"app1/filter_test2.html",context={'dt':dt})
    return response