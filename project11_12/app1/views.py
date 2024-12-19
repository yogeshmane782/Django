from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from app1.models import Product
from app1.forms import ProductForm
from django.urls import reverse_lazy
# Create your views here.
class ProductListView(ListView):
    model=Product
    fields="__all__"
    template_name="app1/prodlist_temp.html"
    context_object_name="products"

class IndexTemplateView(TemplateView):
    template_name="app1/index.html"
class CreateProductView(CreateView):
    model=Product
    template_name="app1/createprod_temp.html"
    success_url=reverse_lazy("prod_list")
    form_class=ProductForm
    msg="Product Added"
