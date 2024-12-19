from django.shortcuts import render
from app1.forms import PersonForm
from django.http import HttpResponse
# Create your views here.

def person_view(request):
    if request.method=="GET":
        pform=PersonForm()
        response=render(request,"app1/person_temp.html",context={'pform':pform})
        return response
    elif request.method=="POST":
        pform=PersonForm(request.POST)
        if pform.is_valid():
            name=pform.cleaned_data['name']
            age=pform.cleaned_data['age']
            city=pform.cleaned_data['city']
            output=f'<h2> {name},{age},{city}</h2>'
            response=HttpResponse(output)
            return response
        else:
            response=render(request,"app1/person_temp.html",context={'pform':pform})
            return response