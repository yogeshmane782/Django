from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from app1.models import App1Product 
# Create your views here.
class AddView(View):
    def get(self,request,*vargs,**kwargs):
        num1=int(request.GET['n1'])
        num2=int(request.GET['n2'])
        num3=num1+num2
        output=HttpResponse(f'Sum of {num1} and {num2} is {num3}')
        return output
    
class AddTemplView(TemplateView):
    template_name="app1/add_temp.html"
class productList(ListView):
    model=App1Product
    template_name="app1/prodlist_temp.html"
    context_object_name='qs'

class productDetail(DetailView):
    model =App1Product
    template_name="app1/proddetail.html"
    context_object_name="qs"
    pk_url_kwarg='pk'