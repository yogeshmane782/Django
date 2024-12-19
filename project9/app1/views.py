from django.shortcuts import render

# Create your views here.
def home(request):
    response=render(request,"app1/index.html")
    return response
def display_sales(request):
    sales_data={2010:45000,
                2011:56000,
                2012:65000,
                2013:70000,
                2014:85000}
    response=render(request,"app1/display_sales.html",context={'sales_data':sales_data})
    return response