from django.shortcuts import render

# Create your views here.
def adding_num(request):
    num1=10
    num2=20
    num3=num1+num2
    d={'num1':num1,'num2':num2,'num3':num3}
    response=render(request,'app1/result.html',context=d)
    return response
