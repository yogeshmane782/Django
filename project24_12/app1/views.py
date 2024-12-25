from django.shortcuts import render
from django.views.generic import CreateView,ListView
from app1.models import Person
from django.http import HttpResponse
# Create your views here.
class PersonView(CreateView):
    model=Person
    fields="__all__"
    template_name="app1/person_temp.html"
    success_url="/home"

def home(request):
    msg="<h2> Image is Uploaded</h2>"
    response=HttpResponse(msg)
    return response
class PersonList(ListView):
    model=Person
    fields="__all__"
    context_object_name="qs"
    template_name="app1/personlist_temp.html"