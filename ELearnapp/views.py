from ast import Return
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from mysqlx import Result
from .models import Vrifylogin,Work,Subject,Announcements,Feedback
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

def addsub(request):
    if request.method == 'POST':
      dptname = request.POST['dptname']
      semno   = request.POST['semno']
      subcode = request.POST['subcode']
      subname = request.POST['subname']
      subcredit = request.POST['subcredit']
      syllabus = request.POST['syllabus']
      tname = request.POST['tname']
      new_sub = Subject(dptname = dptname,semno = semno,subcode = subcode,subname = subname,subcredit = subcredit,syllabus = syllabus,tname = tname)
      new_sub.save()
      return HttpResponse('Added Successfully')
    elif request.method == 'GET':
        return render(request, 'createsub.html')
    else:
        return HttpResponse('Error Occured')
    
def makeannouncement(request):
    if request.method == 'POST':
        announcements=request.POST['announcements']
        new_announcement= Announcements(announcements = announcements)
        new_announcement.save()
        return HttpResponse('Added Successfully')
    elif request.method == 'GET':
        return render(request, 'makeannounce.html')
    else:
        return HttpResponse('Error Occured')
         
def feedback(request):
    if request.method == 'POST':
        feedback = request.POST['feedback']
        new_fb = Feedback(feedback = feedback)
        new_fb.save()
        return HttpResponse('Added Successfully')
    elif request.method == 'GET':
        return render(request,'feedback.html')
    else:
        return HttpResponse('Error Occured')
        

       