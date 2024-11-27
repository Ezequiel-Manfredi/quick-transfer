from django.db import models
from apps.user.models import User

class Account(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
  balance = models.FloatField(default=0.00)
  favorites = models.ManyToManyField('self')
  
  def __str__(self):
    return self.user.username