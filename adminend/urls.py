from django.urls import path
from adminend import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('addadmin/',views.addadmin,name="addadmin"),
    path('SaveAdmin/',views.SaveAdmin,name="SaveAdmin"),
    path('DisplayAdmin/', views.DisplayAdmin, name="DisplayAdmin"),
    path('editadmin/<int:dataid>/', views.editadmin, name="editadmin"),
    path('updatedata/<int:dataid>/', views.updatedata, name="updatedata"),
    path('deletedata/<int:dataid>/', views.deletedata, name="deletedata"),

    path('addwtwedo/',views.addwtwedo,name="addwtwedo"),
    path('savewtwedo/',views.savewtwedo,name="savewtwedo"),
    path('displaywtwedo/', views.displaywtwedo, name="displaywtwedo"),
    path('editwtwedo/<int:dataid>/', views.editwtwedo, name="editwtwedo"),
    path('updatewtwedo/<int:dataid>/', views.updatewtwedo, name="updatewtwedo"),
    path('deletewtwedo/<int:dataid>/', views.deletewtwedo, name="deletewtwedo"),

    path('work/', views.work, name="work"),
    path('saveworks/', views.saveworks, name="saveworks"),
    path('displaywork/', views.displaywork, name="displaywork"),
    path('editwork/<int:dataid>/', views.editwork, name="editwork"),
    path('updatework/<int:dataid>/', views.updatework, name="updatework"),
    path('deletework/<int:dataid>/', views.deletework, name="deletework"),

    path('customertable/', views.customertable, name="customertable"),
    path('deletecustomer/<int:dataid>/', views.deletecustomer, name="deletecustomer"),

    path('consulttable/', views.consulttable, name="consulttable"),
    path('deleteconsult/<int:dataid>/', views.deleteconsult, name="deleteconsult"),

    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout")

]