from django.shortcuts import render

# Create your views here.
def test(request):
    response=render(request,"app1/test.html")
    return response