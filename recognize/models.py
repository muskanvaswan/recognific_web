from django.db import models
from django.utils import timezone
from encode.models import Student, ClassSet


class Attendance(models.Model):
    classname = models.ForeignKey(ClassSet, on_delete=models.CASCADE, related_name="attendees")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendance")
    time = models.DateTimeField(default=timezone.now)


class Marked(models.Model):
    classname = models.ForeignKey(ClassSet, on_delete=models.CASCADE, related_name="marked")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="allowed")
    allow = models.BooleanField(default=False)
