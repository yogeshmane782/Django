from django.shortcuts import render

# Create your views here.
def signin(request):
    users={'naresh':'n123',
    'suresh':'s321',
    'ramesh':'r567'}
    uname=request.GET['uname']
    pwd=request.GET['pwd']
    if uname in users and users[uname]==pwd:
        response=render(request,"app1/welcome.html",context={'uname':uname})
        return response
    else:
        response=render(request,"app1/login.html",context={'msg':"invalid username or password"})
        return response

def login(request):
    response=render(request,"app1/login.html")
    return response