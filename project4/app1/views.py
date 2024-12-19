from django.shortcuts import render

# Create your views here.
def home(request):
    response=render(request,"app1/index.html")
    return response