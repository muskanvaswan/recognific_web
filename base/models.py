from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, related_name='teacher', unique=True, on_delete=models.CASCADE)
    role = models.CharField(blank=True, max_length=200)
