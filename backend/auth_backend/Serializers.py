from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email']
class ProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = ['id','full_name', 'bio','image']       