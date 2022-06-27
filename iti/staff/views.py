from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect,JsonResponse

# Create your views here.
def stafflist(request):
    return HttpResponse('List staff')
def staffinsert(request):
    return JsonResponse({'Name':'Ayat'})
def staffupdate(request):
    return JsonResponse({'Name':'Nadeen'})
def staffdelete(request):
    return HttpResponseRedirect('/listt')
