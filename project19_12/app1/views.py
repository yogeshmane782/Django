from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cart(request):
    b=request.GET['b']
    if b=="AddCart":
        pname=request.GET['pname']
        qty=request.GET['qty']
        if pname not in request.session:
            request.session[pname]=qty
            msg="<h2>ProductAdded to Cart</h2>"
        else:
            msg="This product exists within Cart"
        response=render(request,"app1/index.html",context={'msg':msg})
    elif b=="UpdateCart":
        pname=request.GET['pname']
        qty=request.GET['qty']
        if pname in request.session:
            request.session[pname]=qty
            msg="<h2>Product Updated to Cart</h2>"
        else:
            msg="Invalid ProductName"
        response=render(request,"app1/index.html",context={'msg':msg})
        return response

    elif b=="DeleteCart":
        pname=request.GET['pname']
        if pname in request.session:
            del request.session[pname]
            msg="<h2>Product Deleted from cart</h2>"
        else:
            msg="Invalid ProductName"
        response=render(request,"app1/index.html",context={'msg':msg})
    elif b=="ViewCart":
        output='CartEmpty'
        for pname,qty in request.session.items():
            if output=='CartEmpty':
                output=''
            output+=pname+":"+qty+"<br>"
        response=render(request,"app1/index.html",context={'msg':output})
    return response
def index(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response=render(request,"app1/index.html")
        return response
    else:
        output='''<h2> Please Enablef Cookies</h2>
        <a href='/'>Index</a>'''
        request.session.set_test_cookie()
        response=HttpResponse(output)
        return response
    