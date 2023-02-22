from django.shortcuts import render, redirect
from django.contrib import messages
from adminend.models import admin,consultdb
from userend.models import registerdb


# Create your views here.



def homepage(request):
    return render(request,"homepage.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def homework(req):
    return render(req,"homework.html")
def officework(req):
    return render(req,"officework.html")
def furniturework(req):
    return render(req,"furniturework.html")
def lightwork(req):
    return render(req,"lightwork.html")


def login(req):
    return render(req,"login.html")


def formreg(request):
    if request.method == 'POST':
        na = request.POST.get('username')
        em = request.POST.get('email')
        pa = request.POST.get('password')
        cp = request.POST.get('confirmpassword')
        obj = registerdb(username=na, email=em, password=pa, confirmpassword=cp)
        obj.save()
        messages.success(request, "registered successfully")
        return redirect(login)
    else:
        messages.error(request, "invalid")
        return render(request, "login.html")





def customerlogin(request):
    if request.method == 'POST':
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if registerdb.objects.filter(username=username_r, password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r
            messages.success(request, "login successfully")
            return redirect(homepage)
        else:
            messages.error(request, "invalid user")
            return render(request, "login.html")


def customerlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "logout successfully")
    return redirect(login)


def condet(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        ph = request.POST.get('phone')
        em = request.POST.get('email')
        me = request.POST.get('message')
        obj = admin(name=na,phone=ph, email=em,message=me)
        obj.save()
        messages.success(request, "message delivered")
        return redirect(contact)

def consult(request):
    return render(request,"consult.html")

def consultpage(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        us = request.POST.get('username')
        ph = request.POST.get('phone')
        em = request.POST.get('email')
        me = request.POST.get('message')
        obj = consultdb(name=na,username=us,phone=ph,email=em,message=me)
        obj.save()
        messages.success(request, "Booked successfully")
        return redirect(consult)





