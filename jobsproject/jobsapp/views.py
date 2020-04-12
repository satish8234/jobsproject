from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hydjobs(request):
    s='<h1>Hyderabad jobs information</h1>'
    return HttpResponse(s)

def chennaijobs(request):
    s='<h1>Chennai jobs information</h1>'
    return HttpResponse(s)

def mumbaijobs(request):
    s='<h1>Mumbai jobs information</h1>'
    return HttpResponse(s)

def punejobs(request):
    s='<h1>Pune jobs information</h1>'
    return HttpResponse(s)
