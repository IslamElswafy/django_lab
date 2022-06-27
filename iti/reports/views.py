from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def liststudent(request):
    return HttpResponse('List All Student')

def liststaff(request):
    return HttpResponse('List  All Staff')
def mainreports(request):
    response = HttpResponse()
    response.write('<a href="https://www.google.com/">Google</a>')
    return response


