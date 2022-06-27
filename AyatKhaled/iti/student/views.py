from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect

# Create your views here.
def studentlist(request):
    return HttpResponse('List student')
def studentinsert(request):
    return render (request,'insert.html')
def studentupdate(request):
    return render (request,'update.html')
def studentdelete(request):
    return HttpResponseRedirect('/list')
