from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.ForeignKey(User, related_name='user', unique=True, on_delete=models.CASCADE)
    role = models.CharField(blank=True)
