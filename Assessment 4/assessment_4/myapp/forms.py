from django import forms
from .models import *


class blogform(forms.ModelForm):
    class Meta:
        model=blog_data
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=blog_data
        fields=['Title', 'Author', 'Content']