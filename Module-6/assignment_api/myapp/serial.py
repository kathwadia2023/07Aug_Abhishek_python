from rest_framework import serializers
from .models import *

class stud_ser(serializers.ModelSerializer):
    class Meta:
        model=studinfo
        fields = '__all__'
