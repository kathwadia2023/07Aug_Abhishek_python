from django.contrib import admin
from django.urls import path 
from myapp import views

urlpatterns = [
  
    path('', views.index),
    path('showdata/', views.showdata, name='showdata'),
    path('updatedata/<int:id>', views.update),
    path('deletedata/<int:id>',views.deletedata),

    path('getall/', views.getall, ),
    path('getstud/<int:id>', views.getstud),
    path('deletestud/<int:id>', views.deletestud),

]
