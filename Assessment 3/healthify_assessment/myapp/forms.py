from django import forms
from .models import *


class signupForm(forms.ModelForm):
    class Meta:
        model = usersignup
        fields = '__all__'


class appointment_form(forms.ModelForm):
    class Meta:
        model = appointment
        fields = "__all__"

class update_form(forms.ModelForm):
    class Meta:
        model = usersignup
        fields = ["password"]


class Feedback_form(forms.ModelForm):
    class Meta:
        model = feedback
        fields = "__all__"

class app_g_form(forms.ModelForm):
    class Meta:
        model = app_grant_new
        fields = "__all__"