from django.contrib import admin
from django.urls import path
from myapp import views



urlpatterns = [

    path('', views.index),
    path('appointment/', views.appointment_req, name='appointment'),
    path('profile/',views.profile,name='userlogin'),
    path('about/', views.about),
    path('contact/',views.contact),
    path('user_logout/', views.user_logout),
    path('otp_verify/',views.otp,name='otp'),
    path('resetpass/',views.resetpass, ),
    path('newpass/',views.newpass, name='newpass'),
    path('grantappointment/',views.grantappointment),

]