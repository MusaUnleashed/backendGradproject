  
from rest_framework import serializers
from .models import My_Test
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class My_TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = My_Test
        fields = ( 'title', 'test_id', 'test_owner')
