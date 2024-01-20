from django.contrib import admin
from django.urls import path, include
from myapp import views
urlpatterns = [
  
    path('getall/', views.getall ),
    path('getstud/<int:id>', views.getstud),
    path('deletestud/<int:id>', views.deletestud),

]
