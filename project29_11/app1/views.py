from django.shortcuts import render
from app1.forms import RegisterForms
# Create your views here.
def register_temp(request):
    f1=RegisterForms()
    response=render(request,"app1/register.html",context={'f1':f1})
    return response