from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from student.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin ,logout as authlogout
# Create your views here.
def home(req):
    return render(req,'index.html')



def login(req):
    # req.session.clear()
    if(req.session.get('username') is None):
        if(req.method=='GET'):
            return render(req, 'loginform.html')
        else:
            myuserobject= MyUser.objects.filter(username=req.POST['username'],password=req.POST['password'])
            authuserobject=authenticate(username=req.POST['username'],password=req.POST['password'])
            if(len(myuserobject)>0 and authuserobject is not None):
                req.session['username']=myuserobject[0].username
                authlogin(req,authuserobject)
                return render(req, 'index.html')
            else:
                context={}
                context['error']='invalid username or password'

                return render(req, 'loginform.html',context)
    else:
        return render(req,'index.html')


def singup(req):
    if (req.method=='GET'):
        return render(req,'sign_up.html')
    else:
        U=MyUser.objects.create(username=req.POST['username'],email=req.POST['email'],password=req.POST['password'])
        User.objects.create_user(username=req.POST['username'],email=req.POST['email'],password=req.POST['password'],is_superuser=True,is_staff=True)
        return render(req,'loginform.html')



def logout(req):
    if (req.session.get('username') is None and req.user.is_authenticated()):
            req.session.clear()
            authlogout(req,req.user)
    else:
        return render(req,'loginform.html')
