from api.models import *
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email']
class ProfileSerializer(serializers.MOdelSerializer):
    class Meta:
        model = Profile
        fields = ['id','user','full_name','bio','image','verified']        
