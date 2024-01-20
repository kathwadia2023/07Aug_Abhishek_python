from django.contrib import admin
from .models import *
# Register your models here.

class studData(admin.ModelAdmin):
    list_display=['id','Title','Author','Isbn', 'Publisher']


admin.site.register(studinfo,studData)