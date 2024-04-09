from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path 
from api import views

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('dashbord/', views.dashbord),
    path("todo/<user_id>/", views.TodoListView.as_view()),
    path('todo-detail/<user_id>/<todo_id>/', views.TodoDetailView.as_view()),
    path('todo-mark-as-completed/<user_id>/<todo_id>/', views.TodoMarkAsCompleted.as_view()),

]

