from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from app1.models import Employee
# Create your views here.
class EmpListView(ListView):
    model=Employee
    fields='__all__'
    template_name="app1/emplist.html"
    context_object_name='qs'
    def get_queryset(self):
        job=self.request.GET['job']
        qs=Employee.objects.filter(job=job)
        return qs
class TemplateView(TemplateView):
    template_name="app1/index.html"