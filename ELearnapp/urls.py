from django.contrib import admin
from django.urls import path
from .views import studregview

urlpatterns = [
    path('admin/',studregview,name='studentregistration')
]
