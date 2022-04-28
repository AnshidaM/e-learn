from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from ELearnapp.models import teachers
from mysqlx import Result
# Create your views here.

def showsubsonaddworks(request):
    results=teachers.objects.all
    return render(request,"addworks.html",{"showsubs":results})

def showdepsonaddworks(request):
    results=teachers.objects.all
    return render(request,"addworks.html",{"showdeps":results})


def studregview(request):
    return render(request,"studreg.html")
