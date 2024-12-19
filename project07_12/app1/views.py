from django.shortcuts import render
from app1.forms import ProductForm
from app1.models import Product
# Create your views here.
def home(request):
    response=render(request,"app1/index.html")
    return response
def addproid_view(request):
    if request.method=="GET":
        prod_form=ProductForm()
        response=render(request,"app1/addprod_temp.html",context={'prod_form':prod_form})
        return response
    elif request.method=="POST":
        prod_form=ProductForm(request.POST)
        if prod_form.is_valid():
            prod_form.save(commit=True)
            prod_form=ProductForm()
            msg="Product Added"
            response=render(request,"app1/addprod_temp.html",context={'prod_form':prod_form,'msg':msg})
            return response
        else:
            response=render(request,"app1/addprod_temp.html",context={'prod_form':prod_form})
            return response
        
def listprod_view(request):
    data=Product.objects.all()
    response=render(request,"app1/listprod_temp.html",context={'data':data})
    return response
def prodedit_view(request,pid=None):
    if request.method=="GET":
        prod=Product.objects.get(proid=pid)
        prod_form=ProductForm(instance=prod)
        response=render(request,"app1/prodedit_temp.html",context={'prod_form':prod_form})
        return response
def saveprod_view(request):
    if request.method=="POST":
        prod=Product.objects.get(proid=request.POST['proid'])
        prod_form=ProductForm(request.POST,instance=prod)
        if prod_form.is_valid():
            prod_form.save(commit=True)
            msg="Product Updated"
        response=render(request,"app1/prodedit_temp.html",context={'prod_form':prod_form,'msg':msg})
        return response
def proddelete_view(request,pid):
    prod=Product.objects.get(proid=pid)
    prod.delete()
    response=render(request,"app1/index.html",context={'msg':'Product Deleted'})
    return response