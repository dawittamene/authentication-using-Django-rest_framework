from django.shortcuts import render
from rest_frame_work.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

from api.models import *
from api.Serializer import *

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

