from django.shortcuts import render

# Create your views here.
def home(request):
    response=render(request,"app1/index.html")
    return response
def courses(request):
    data=[]
    for c in request.GET.keys():
        data.append(request.GET[c])
    if len(data)==0:
        data=None
    response=render(request,"app1/find_fee.html",context={'data':data})
    return response