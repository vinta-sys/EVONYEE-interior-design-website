from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from adminend.models import admindb,wtwedodb,workdb,admin,consultdb


# Create your views here.

def index(request):
    return render(request, "index.html")
def addadmin(req):
    return render(req, "addadmin.html")
def SaveAdmin(request):
    if request.method == 'POST':
        na = request.POST.get('Name')
        po = request.POST.get('position')
        em = request.POST.get('Email')
        mo = request.POST.get('Mobile')
        us = request.POST.get('Username')
        pa = request.POST.get('Password')
        img = request.FILES['image']
        obj = admindb(Name=na,position=po, Email=em, Mobile=mo, Username=us, Password=pa, image=img)
        obj.save()
        messages.success(request, "saved successfully")
        return redirect(addadmin)

def DisplayAdmin(request):
    data = admindb.objects.all()
    return render(request, "DisplayAdmin.html", {'data': data})

def editadmin(req, dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(req, "editadmin.html", {'data':data})

def updatedata(request,dataid):
    if request.method== 'POST':
        na = request.POST.get('Name')
        po = request.POST.get('position')
        em = request.POST.get('Email')
        mo = request.POST.get('Mobile')
        us = request.POST.get('Username')
        pa = request.POST.get('Password')
        try:
            img=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= admindb.objects.get(id=dataid).image
        admindb.objects.filter(id=dataid).update(Name=na,position=po, Email=em, Mobile=mo, Username=us, Password=pa, image=file)
        messages.success(request, "saved successfully")
        return redirect(DisplayAdmin)

def deletedata(request, dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted successfully")
    return redirect(DisplayAdmin)



def addwtwedo(req):
    return render(req, "wtwedo.html")
def savewtwedo(request):
    if request.method == 'POST':
        na = request.POST.get('Name')
        img = request.FILES['image']
        obj = wtwedodb(Name=na,image=img)
        obj.save()
        messages.success(request, "saved successfully")
        return redirect(addwtwedo)

def displaywtwedo(request):
    data = wtwedodb.objects.all()
    return render(request, "displaywtwedo.html", {'data': data})

def editwtwedo(req, dataid):
    data = wtwedodb.objects.get(id=dataid)
    print(data)
    return render(req, "editwtwedo.html", {'data':data})

def updatewtwedo(request,dataid):
    if request.method== 'POST':
        na = request.POST.get('Name')
        try:
            img=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= wtwedodb.objects.get(id=dataid).image
        wtwedodb.objects.filter(id=dataid).update(Name=na,image=file)
        messages.success(request, "saved successfully")
        return redirect(displaywtwedo)

def deletewtwedo(request, dataid):
    data = wtwedodb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted successfully")
    return redirect(displaywtwedo)

def work(request):
    data=wtwedodb.objects.all()
    return render(request, "work.html", {'data':data} )


def saveworks(request):
    if request.method == 'POST':
        ca = request.POST.get('category')
        em = request.POST.get('description')
        img = request.FILES['Image']
        obj = workdb(category=ca,description=em, Image=img)
        obj.save()
        messages.success(request, "saved successfully")
        return redirect(work)
def displaywork(request):
    data = workdb.objects.all()
    return render(request, "displaywork.html", {'data': data})
def editwork(req, dataid):
    data = workdb.objects.get(id=dataid)
    da = wtwedodb.objects.all()
    print(data)
    return render(req, "editwork.html", {'data':data, 'da':da})

def updatework(request,dataid):
    if request.method== 'POST':
        ca = request.POST.get('category')
        em = request.POST.get('description')

        try:
            img=request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file= workdb.objects.get(id=dataid).Image
        workdb.objects.filter(id=dataid).update(category=ca,description=em, Image=file)
        messages.success(request, "saved successfully")
        return redirect(displaywork)

def deletework(request, dataid):
    data = workdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted successfully")
    return redirect(displaywork)

def consulttable(request):
    data = consultdb.objects.all()
    return render(request, "consulttable.html", {'data': data})
def deleteconsult(request, dataid):
    data = consultdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted successfully")
    return redirect(consulttable)

def customertable(request):
    data = admin.objects.all()
    return render(request, "customertable.html", {'data': data})
def deletecustomer(request, dataid):
    data = admin.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted successfully")
    return redirect(customertable)


def loginpage(req):
    return render(req,"loginpage.html")

def adminlogin(rqst):
    if rqst.method == "POST":
        username_r = rqst.POST.get('username')
        password_r = rqst.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(rqst, user)
                rqst.session['username']=username_r
                rqst.session['password']=password_r
                messages.success(rqst, "login successfully")
                return redirect(index)
            else:
                messages.error(rqst, "invalid user")
                return render(rqst, "loginpage.html")
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "logout successfully")
    return redirect(loginpage)
