from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#function based view

def first(request):
    return HttpResponse("first page")

def second(request):
    return HttpResponse("second page")
