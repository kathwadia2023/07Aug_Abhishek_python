from django.db import models

# Create your models here.
class signupmaster(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    wing = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    block = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
