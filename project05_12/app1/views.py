from django.shortcuts import render
from app1.forms import UserForm
from django.http import HttpResponse

# Create your views here.
def user_view(request):
    if request.method=="GET":
        user=UserForm()
        response=render(request,"app1/user_temp.html",context={'user_form':user})
        return response
    elif request.method=="POST":
        user=UserForm(request.POST)
        if user.is_valid():
            name=user.cleaned_data['name']
            uname=user.cleaned_data['uname']
            email=user.cleaned_data['email']
            output=f'<h2>{name},{uname},{email}</h2>'
            response=HttpResponse(output)
            return response
        else: 
            response=render(request,"app1/user_temp.html",context={'user_form':user})
            return response
        