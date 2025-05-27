from django.shortcuts import render
from app1.models import Users,Mail
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,"app1/index.html")
def main(request):
    btn=request.GET['btn']
    if btn=="Signin":
        response=render(request,"app1/signin.html")
    elif btn=='Signup':
        response=render(request,"app1/signup.html")
    return response
def signup(request):
    name=request.POST['name']
    uname=request.POST['uname']
    password=request.POST['pwd']
    user=Users(name=name,uname=uname,password=password)
    try:
        user.save()
        response=render(request,"app1/index.html",context={'msg':'User Registered...'})
    except:
        response=render(request,"app1/signup.html",context={'msg':'Error Registering User...'})
    return response
def signin(request):
    username=request.POST['uname']
    password=request.POST['pwd']
    try:
        user=Users.objects.get(Q(uname=username)&Q(password=password))
        response=render(request,"app1/user_dashboard.html",context={'request':request})
        request.session['uname']=username
    except:
        msg="Invalid UserName or Password"
        response=render(request,"app1/signin.html",context={'msg':msg})
    return response
def inbox(request):
    uname=request.session['uname']
    qs=Mail.objects.filter(to_user=uname)
    response=render(request,"app1/inbox.html",context={'qs':qs})
    return response
def compose_temp(request):
    return render(request,"app1/compose_temp.html")
def receive_mail(request):
    to=request.GET['to']
    message=request.GET['message']
    fr=request.session['uname']
    try:
        user=Users.objects.get(uname=to)
        mail_obj=Mail(from_user=fr,to_user=user,content=message.strip())
        mail_obj.save()
        response=render(request,"app1/user_dashboard.html",context={'msg':'Mail Sent'})
    except:
        response=render(request,"app1/user_dashboard.html",context={'msg':'Error in sending message'})
    return response
def signout(request):
    if 'uname' in request.session:
        del request.session['uname']
        response=render(request,"app1/index.html")
        return response
    else:
        response=render(request,"app1/index.html")
        return response