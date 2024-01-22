from django.db import models

# Create your models here.

class blog_data(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=20)
    Content = models.CharField(max_length=300)
    # updated = models.DateTimeField(auto_now_add=True)

    
