from django.shortcuts import render
from django.views.generic import CreateView,ListView
from app1.models import Student
from django.http import HttpResponse
# Create your views here.
class StudentView(CreateView):
    model=Student
    fields="__all__"
    template_name="app1/student_temp.html"
    success_url='/home'
def home(request):
    msg="<h2>Images is uploaded</h2>"
    response=HttpResponse(msg)
    return response
class StudentList(ListView):
    model=Student
    fields="__all__"
    context_object_name="qs"
    template_name="app1/studentlist_temp.html"