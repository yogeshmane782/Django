from django.shortcuts import render
from app1.models import *
from django.db.models import *
# Create your views here.
def home(request):
    response=render(request,"app1/index.html")
    return response
def main_view(request):
    b1=request.POST['b1']
    if b1=="Signin":
        response=render(request,"app1/signin.html")
    elif b1=="Signup":
        response=render(request,"app1/signup.html")
    return response
def signin_view(request):
    uname=request.POST['uname']
    pwd=request.POST['pwd']
    try:
        user=Users.objects.get(Q(uname=uname)&Q(password=pwd))
        response=render(request,"app1/dashboard.html",context={'request':request})
        request.session['uname']=uname
    except:
        msg="Invalid username and password"
        response=render(request,"app1/dashboard.html",contest={'msg':msg})
    return response
def signup_view(request):
    name=request.POST['name']
    uname=request.POST['uname']
    pwd=request.POST['pwd']
    user=Users(name=name,uname=uname,password=pwd)
    try:
        user.save()
        response=render(request,"app1/index.html",context={'msg':"User Registered..."})
    except:
        response=render(request,"app1/signup.html",context={'msg':'Error Registering User'})
    return response
def signout_view(request):
    response=render(request,"app1/index.html")
    return response
def receive_mail(request):
    to=request.GET['to']
    message=request.GET['message']
    fr=request.session['uname']
    try:
        user=Users.objects.get(uname=to)
        mail_obj=Mails(from_user=fr,to_user=user,content=message.strip())

        mail_obj.save()
        response=render(request,"app1/dashboard.html",context={'msg':'Mail sent'})
    except:
        response=render(request,"app1/dashboard.html",context={'msg':'Error in sending message'})
    return response
def compose_view(request):
    response=render(request,"app1/compose_temp.html")
    return response
def inbox(request):
    uname=request.session['uname']
    qs=Mails.objects.filter(to_user=uname)
    responsee=render(request,"app1/inbox_temp.html",context={'qs':qs})
    return responsee