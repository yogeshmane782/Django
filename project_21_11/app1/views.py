from django.shortcuts import render
from app1.models import Marks

# Create your views here.
def home(request):
    response=render(request,"app1/index.html")
    return response
def add_student_template(request):
    response=render(request,"app1/add_student.html")
    return response
def add_student(request):
    rno=int(request.GET['rno'])
    name=request.GET['name']
    s1=float(request.GET['sub1'])
    s2=float(request.GET['sub2'])
    m=Marks(rollno=rno,name=name,sub1=s1,sub2=s2)
    m.save()
    response=render(request,"app1/add_student.html",context={'msg':'Student Added'})
    return response
def update_template(request):
    response=render(request,"app1/update_student.html")
    return response
def update_student(request):
    rno=int(request.GET['rno'])
    s1=float(request.GET['sub1'])
    s2=float(request.GET['sub2'])
    try:
        stud=Marks.objects.get(rollno=rno)
        stud.sub1=s1
        stud.sub2=s2
        stud.save()
        response=render(request,"app1/update_student.html",context={'msg':'Marks Updated'})
    except:
        response=render(request,"app1/update_student.html",context={'msg':'Invalid Rollno'})
    return response
def find_result_template(request):
    response=render(request,"app1/find_result.html")
    return response
def find_result(request):
    rno=int(request.GET['rno'])
    try:
        stud=Marks.objects.get(rollno=rno)
        result="PASS" if stud.sub1>=40 and stud.sub2>=40 else "FAIL"
        response=render(request,"app1/show_result.html",context={'stud':stud,"result":result})
    except:
        response=render(request,"app1/find_result.html",context={'msg':'invalid rno'})
    return response
def delete_student_template(request):
    response=render(request,"app1/delete_student.html")
    return response
def delete_student(request):
    rno=int(request.GET['rno'])
    try:
        stud=Marks.objects.get(rollno=rno)
        stud.delete()
        response=render(request,"app1/delete_student.html",context={'msg':'student deleted'})
    except:
        response=render(request,"app1/delete_student.html",context={'msg':'invalid rollno'})
    return response
def view_student(request):
    qs=Marks.objects.all()
    response=render(request,"app1/view_students.html",context={"qs":qs})
    return response