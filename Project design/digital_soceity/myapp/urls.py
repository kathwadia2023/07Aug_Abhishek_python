from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('contact/', views.contact),
    path('gogreen/', views.gogreen),
    path('event/', views.event),
    path('com_member/', views.com_member),
    

]