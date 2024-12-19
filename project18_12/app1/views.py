from django.shortcuts import render

# Create your views here.
def count_view(request):
    count=request.session.get('count',0)
    if count==0:
        request.session['count']=1
    else:
        request.session['count']+=1
    count=request.session['count']
    response=render(request,"app1/index.html",context={'count':count})
    return response
def index(request):
    response=render(request,"app1/index.html")
    return response
