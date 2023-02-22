from django.urls import path
from userend import views

urlpatterns =[

    path('',views.homepage,name="homepage"),
    path('contact/',views.contact,name="contact"),
    path('about/', views.about, name="about"),
    path('homework/', views.homework, name="homework"),
    path('officework/', views.officework, name="officework"),
    path('furniturework/', views.furniturework, name="furniturework"),
    path('lightwork/', views.lightwork, name="lightwork"),
    path('login/', views.login, name="login"),
    path('formreg/', views.formreg, name="formreg"),
    path('customerlogin/', views.customerlogin, name="customerlogin"),
    path('customerlogout/', views.customerlogout, name="customerlogout"),
    path('condet/', views.condet, name="condet"),
    path('consult/', views.consult, name="consult"),
    path('consultpage/', views.consultpage, name="consultpage")

]