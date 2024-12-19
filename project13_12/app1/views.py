from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from app1.models import Product
from django.urls import reverse,reverse_lazy
# Create your views here.
class templateview(TemplateView):
    template_name="app1/index.html"
class createproductview(CreateView):
    model=Product
    fields='__all__'
    template_name="app1/createprod.html"
    success_url=reverse_lazy('ulist')

