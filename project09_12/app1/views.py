from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

#Function base view
def welcome_view(request):
    respone=render(request,"app1/welcome.html")
    return respone

#Class based view
class welcomeview2(TemplateView):
    template_name="app1/welcome1.html"