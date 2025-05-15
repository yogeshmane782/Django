from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.forms import SignupForm

# Create your views here.
def welcome(request):
    output="<h2>Hello Welcome</h2>"
    response=HttpResponse(output)
    return response
def signup(request):
    if request.method=='GET':
        form=SignupForm()
        response=render(request,"app1/signup.html",context={'form':form})
        return response
    elif request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            response=redirect("login")
    else:
        response=render(request,"app1/signup.html")
        return response

