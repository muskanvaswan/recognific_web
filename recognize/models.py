from django.db import models

from encode.models import Student, ClassSet


class Attendance(models.Model):
    classname = models.ForeignKey(ClassSet, on_delete=models.CASCADE, related_name="attendees")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendance")
    time = models.DateTimeField(auto_now_add=True)
