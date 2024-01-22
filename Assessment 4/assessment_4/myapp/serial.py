from rest_framework import serializers
from .models import *

class blog_ser(serializers.ModelSerializer):
    class Meta:
        model=blog_data
        fields = '__all__'
