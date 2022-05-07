from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('addwork/', views.addwork, name='addwork'),
]
