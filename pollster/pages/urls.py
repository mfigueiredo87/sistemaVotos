from django.urls import path

from . import views

#add a namespace

urlpatterns = [
    path('', views.index, name='index')
    
]