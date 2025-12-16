from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100,unique=True)
    user_bio = models.CharField(max_length=100 )
    profile_image = models.ImageField(upload_to="profile")
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "phone_number" # use phone number field for login
    REQUIRED_FIELDS=[]