from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login_view(request):
    uname=request.GET['uname']
    response=render(request,"app1/inbox.html")
    response.set_cookie("uname",uname)
    return response
def inbox_view(request):
    uname=request.COOKIES['uname']
    output=f'''<h2>{uname}</h2>,
<h2> This is your inbox</h2>'''
    response=HttpResponse(output)
    return response
def home(request):
    response=render(request,"app1/login.html")
    return response