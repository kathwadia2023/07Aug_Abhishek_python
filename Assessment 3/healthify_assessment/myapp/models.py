from django.db import models

# Create your models here.
class usersignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    mobile = models.BigIntegerField()

class appointment(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    patient_name = models.CharField(max_length=20) 
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    health_issue = models.CharField(max_length=20)
    doctor_name=models.CharField(max_length=20)
    my_files = models.FileField(upload_to='Healthify')
    comments = models.TextField()


class feedback(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    sub = models.CharField(max_length=20)
    msg = models.TextField()

class app_grant(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    p_name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.CharField(max_length=20)
    
class app_grant_new(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    p_name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.CharField(max_length=20)
    email = models.EmailField()