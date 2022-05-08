from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addwork/', views.addwork, name='addwork'),
    path('addsub/', views.addsub, name='addsub'),
    path('makeannouncement/', views.makeannouncement, name='makeannouncement'),
    path('feedback/', views.feedback, name='feedback'),
]
