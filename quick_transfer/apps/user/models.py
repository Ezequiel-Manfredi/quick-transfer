from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    dni = models.IntegerField()
    img_profile = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_admin = models.BooleanField(default=False)