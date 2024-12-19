from django.shortcuts import render

# Create your views here.
def cart_view(request):
    b1=request.GET['b1']
    if b1=="AddtoCart":
        pname=request.GET['pname']
        qty=request.GET['qty']
        response=render(request,"app1/index.html",context={'msg':"Product Added to Cart"})
        response.set_cookie(pname,qty)
        return response 
    elif b1=="UpdatetoCart":
        pname=request.GET['pname']
        qty=request.GET['qty']
        response=render(request,"app1/index.html",context={'msg':"Product Updated to Cart"})
        response.set_cookie(pname,qty)
        return response
    
    elif b1=="DeletefromCart":
        pname=request.GET['pname']
        qty=request.GET['qty']
        response=render(request,"app1/index.html",context={'msg':"Product Deleted from Cart"})
        response.delete_cookie(pname)
        return response 
    
    elif b1=="ViewCart":
        output=''
        for pname,qty in request.COOKIES.items():
            output=output+pname+":"+qty+"<br>"
        response=render(request,"app1/index.html",context={'msg':output})
        return response 


def index(request):
    response=render(request,"app1/index.html")
    return response 


