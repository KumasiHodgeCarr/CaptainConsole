from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    profile_image = models.CharField(max_length=9999)



