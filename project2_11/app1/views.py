from django.shortcuts import render

# Create your views here.
def student_view(request):
    stud_data={'naresh':[30,54],
               'suresh':[56,57],
               'ramesh':[88,89]}
    response=render(request,"app1/result.html",context={"stud_data":stud_data})
    return response