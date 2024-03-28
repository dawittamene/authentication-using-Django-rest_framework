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
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token=super().get_token(user)
        
        
        token['full_name'] = user.profile.full_name
        token['username'] = user.username
        token['email'] = user.email
        token['bio'] = user.profile.bio
        token['image'] = user.profile.image
        token['verified'] = user.profile.verified
        
        return token

class ReigsterSerialzer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])   
    confirm_password = serializers.CharField(write_only=True, required=True)   
    
    class Meta:
        model = User
        fields = ['email','username', 'password', 'confirm_password']
        
        
        def validate(self, attrs):
            if attrs ['password']!=attrs['confirm_password']:
                raise serializers.ValidationError(
                    {'password':'password fields does not match'}
                )
            return attrs
        def create(self, validated_data):
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                
            )    
            user.set_password(validated_data['password'])
            user.save()
            return user