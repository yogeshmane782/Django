from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=CustomUserCreationForm()
    return render(request,"app1/register.html",{'form':form})
def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password1=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,"app1/login.html",{'error':'Invalid Creditials'})
    return render(request,"app1/login.html")
def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def home(request):
    return render(request,'app1/home.html')