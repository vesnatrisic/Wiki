from . import views
from django.urls import path 

urlpatterns = [
    path ("", views.index, name="index"),
    path ("Python", views.python, name="python"),
    path ("CSS", views.css, name="css"),
    path ("Django", views.django, name="django"),
    path ("GIT", views.git, name="git"),
    path ("HTML", views.html, name="html"),
    path ("latestNews", views.latestNews, name="latestNews"),
    path ("createNewPage", views.createNewPage, name="createNewPage")
]