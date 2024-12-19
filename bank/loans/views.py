from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def loan_elg(request):
    output='''<HTML>
    <BODY bgcolor=green>
    <H2>loan elg</H2>
    </BODY>
    </HTML>'''
    response=HttpResponse(output)
    return response