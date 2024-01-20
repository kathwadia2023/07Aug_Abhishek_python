from django.db import models

# Create your models here.

class studinfo(models.Model):
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=20)
    Isbn = models.BigIntegerField()
    Publisher = models.CharField(max_length=20)
    
