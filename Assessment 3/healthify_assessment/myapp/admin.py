from django.contrib import admin
from .models import *

# Register your models here.


class userdata(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','role','firstname','lastname','email','city','state','mobile']

admin.site.register(usersignup,userdata)