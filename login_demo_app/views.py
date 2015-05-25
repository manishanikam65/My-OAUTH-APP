from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def login(request):
     return render(request, 'login_demo_app/login.html', {"user":request.user})


def logged(request):
    return render(request,"login_demo_app/logged.html",{"user":request.user})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")