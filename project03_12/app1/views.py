from django.shortcuts import render
from app1.forms import StudentForm
from django.http import HttpResponse
# Create your views here.
def stud_view(request):
    if request.method=="GET":
        stud_form=StudentForm()
        response=render(request,"app1/stud_temp.html",context={'stud_form':stud_form})
        return response
    elif request.method=="POST":
        rollno=request.POST['rollno']
        name=request.POST['name']
        course=request.POST['course']
        fee=request.POST['fee']
        output=f'{rollno},{name},{course},{fee}'
        response=HttpResponse(output)
        return response
