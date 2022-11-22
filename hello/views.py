
from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    return render (request, "hello/index.html")

def python(request):
    return render (request, "hello/python.html")
