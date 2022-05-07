from ast import Return
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from mysqlx import Result
from .models import Vrifylogin,Work
# Create your views here.

def addwork(request):
    if request.method == 'POST':
        workid = request.POST['workid']
        dptname = request.POST['dptname']
        subname = request.POST['subname']
        defwork = request.POST['defwork']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        new_work = Work(workid = workid,dptname = dptname,subname = subname,defwork = defwork,sdate = sdate,edate = edate)
        new_work.save()
        return HttpResponse('Added Successfully')
    elif request.method == 'GET':
        return render(request, 'addworks.html')
    else:
        return HttpResponse('Error Occure')


       