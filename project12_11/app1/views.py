from django.shortcuts import render

# Create your views here.
def display_data_upper(request):
    list_names=["naresh","suresh","ramesh","kishore"]
    response=render(request,"app1/display_data_upper.html",context={'list_names':list_names})
    return response
def display_data_lower(request):
    list_names=["NARESH","SURESH","RAMESH","RAJESH"]
    response=render(request,"app1/display_data_lower.html",context={'list_names':list_names})
    return response
def display_data_title(request):
    list_names=["suresh gupta","rohit sharma"]
    response=render(request,"app1/display_data_title.html",context={'list_names':list_names})
    return response