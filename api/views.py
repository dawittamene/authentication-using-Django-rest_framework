from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import generics,  status
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.shortcuts import get_object_or_404
from api.models import *
from api.Serializer import *

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()    
    permission_classses = [AllowAny]
    serializer_class = RegisterSerializer

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
    
class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = User.objects.get(id=user_id)

        todo = Todo.objects.filter(user=user) 
        return todo
        
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    
    def get_object(self):
        user_id = self.kwargs['user_id']
        todo_id = self.kwargs['todo_id']
        queryset = Todo.objects.filter(user_id=user_id, id=todo_id)
        return get_object_or_404(queryset) 


class TodoMarkAsCompleted(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    
    def get_object(self):
        user_id = self.kwargs['user_id']
        todo_id = self.kwargs['todo_id']
        user = User.objects.get(id=user_id)  # Assuming you have a User model
        todo = Todo.objects.get(id=todo_id, user=user)  # Using get() instead of filter()
        todo.completed = True  # Assuming you have a completed field in your Todo model
        todo.save()
        return todo
        
    
    