from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER_ROLES = (
        ('admin', 'System Admin'),
        ('provider', 'Service Provider'),
        ('seeker', 'Service Seeker'),
    )
    role = models.CharField(max_length=10, choices=USER_ROLES)
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['role', 'email', 'first_name', 'last_name']
    USERNAME_FIELD = 'username'  # can be changed to email later

    class Meta:
        db_table = 'customuser'


    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)

    class Meta:
        db_table = 'userprofile'

    def __str__(self):
        return f"{self.user.username}'s Profile"