from django.shortcuts import render

# Create your views here.
students_data={}
def home(request):
    response=render(request,"app1/index.html")
    return response
def add_student(request):
    sname=request.GET['name']
    scourse=request.GET['course']
    sfee=request.GET['fee']
    students_data[sname]=[scourse,sfee]
    response=render(request,"app1/index.html",context={"msg":"studentAdded"})
    return response
def display_student(request):
    response=render(request,"app1/display_student.html",context={'students_data':students_data})
    return response
def add_template(request):
    response=render(request,"app1/add_student.html")
    return response