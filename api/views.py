from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny,IsAuthenticated

from api.models import *
from api.Serializer import *

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()    
    permission_classses = [AllowAny]
    serializer_class = ReigsterSerialzer

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def dashbord(request):
    if request.methode == 'GET':
        response = f"Hey {request.user}, You are seeing Get response "
        return Response({'response':response}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get("text")
        response = f"Hey {request.user}, You are seeing Post response {text}"
        return Response({'response':response}, status=status.HTTP_200_OK)
    
    return Response({}, status=status.HTTP_400_BAD_REQUEST)
    
        
        