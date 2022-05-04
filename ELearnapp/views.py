from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from mysqlx import Result
# Create your views here.

def homepageview(request):
    return render(request,"ELearnapp/login.html")
