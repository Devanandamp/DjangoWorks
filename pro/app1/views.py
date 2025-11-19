from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#class based view

#function based view

# def home(request):
#     return HttpResponse("Welcome to Django")
#
# def index(request):
#     return HttpResponse("index page")
#
# def new(request):
#     return HttpResponse("Hello new page")


def home(request):

    context = {'name':'Arun','age':25}
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

