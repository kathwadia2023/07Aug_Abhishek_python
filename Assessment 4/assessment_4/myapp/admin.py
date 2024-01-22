from django.contrib import admin
from .models import *
# Register your models here.

class blog(admin.ModelAdmin):
    list_display=['id','Title','Author', 'Content']


admin.site.register(blog_data,blog)