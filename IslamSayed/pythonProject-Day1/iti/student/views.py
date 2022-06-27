from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.
def list(req):
    return HttpResponse('student list </br> 1- update </br>2- instal')
def home(req):
    return render(req,'pass.html')
def update(req):
    return render(req,'update.html')
def insert(req):
    return render(req,'index.html')
def delet(req):
    return HttpResponseRedirect('/list')
