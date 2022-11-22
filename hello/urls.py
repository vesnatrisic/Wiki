from . import views
from django.urls import path 

urlpatterns = [
    path ("", views.index, name="index"),
    path ("Python", views.python, name="python")
]