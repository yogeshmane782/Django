from django.shortcuts import render

# Create your views here.
def list_product(request):
    product_data={'mouse':[100,'mouse.jpg'],
                  'keyboard':[2000,'keyboard.jpg'],
                  'monitor':[5000,'monitor.jpg']}
    response=render(request,"app1/list_product.html",context={'product_data':product_data})
    return response