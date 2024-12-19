from django.shortcuts import render

# Create your views here.
def home(request):
    response=render(request,"app1/index.html")
    return response

def student_view(request):
    stud_data={'naresh':[50,60],
               'suresh':[60,70],
               'ramesh':[30,40]
               }
    response=render(request,"app1/result.html",context={'stud_data':stud_data})
    return response