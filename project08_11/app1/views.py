from django.shortcuts import render

# Create your views here.
def list_students(request):
    students_data={101:["Yogesh","Python","yogesh.jpg"],
                  102:["Abhi","Python","abhi.jpg"],
                  103:["Thokal",".Net","thokal.jpg"]}
    reponse=render(request,"app1/list_students.html",context={'students_data':students_data})
    return reponse