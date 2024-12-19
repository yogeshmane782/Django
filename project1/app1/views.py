from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greeting(request):
    str1='<h1>Welcome to Django </h1>'
    response=HttpResponse(str1)
    return response
