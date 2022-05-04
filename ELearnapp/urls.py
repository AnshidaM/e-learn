from django.contrib import admin
from django.urls import path
from .views import homepageview

urlpatterns = [
    path('',homepageview,name = 'homepage'),
]
