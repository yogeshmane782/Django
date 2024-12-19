from django.shortcuts import render

# Create your views here.
def view_image(request):
    response=render(request,"app1/Imageview.html")
    return response
               