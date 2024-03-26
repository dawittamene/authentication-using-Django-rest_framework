from django.contrib.auth.models import AbstractUser, Group as AuthGroup, Permission as AuthPermission
from django.db import models
from django.db.models.signals import post_save

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    groups = models.ManyToManyField(
        AuthGroup,
        related_name='custom_users',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        AuthPermission,
        related_name='custom_users',
        blank=True
    )

    
    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False) 
    