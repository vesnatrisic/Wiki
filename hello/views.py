
from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    return render (request, "hello/index.html")

def python(request):
    return render (request, "hello/python.html")

def css(request):
    return render (request, "hello/css.html")

def django(request):
    return render (request, "hello/django.html")

def git(request):
    return render (request, "hello/git.html")

def html(request):
    return render (request, "hello/html.html")

def latestNews(request):
    return render (request, "hello/latestNews.html")


