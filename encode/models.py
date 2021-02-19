from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_init, post_delete
from django.dispatch import receiver

import numpy as np
import pickle
import json
import time
import os

from .encodings import encode_image, make_encodings


class Student(models.Model):
    user = models.OneToOneField(User,  related_name='student', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/students')
    encodings = models.JSONField(blank=True, null=True)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"{self.id} {self.user.get_full_name()}"


class ClassSet(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ManyToManyField(User, blank=True, related_name="classes")
    students = models.ManyToManyField(Student, related_name='classname')
    active = models.BooleanField(default=False)
    occourance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} by {self.teacher}"

    def get_file_url(self):
        return f"/media/Attendance/sheet_{self.id}.xlsx"

    def activate(self):
        self.active = True
        self.occourance += 1
        for m in self.marked.all():
            m.allow = True
            m.save()
        self.save()

    def deactivate(self):
        self.active = False
        self.save()


@receiver(post_save, sender=ClassSet)
def my_handler(sender, **kwargs):
    print(kwargs.get("created"))
    make_encodings(kwargs.get("instance"))


@receiver(post_save, sender=Student)
def student_save_handler(sender, **kwargs):
    instance = kwargs.get('instance')
    if kwargs.get('created') == True:
        print("here")
        instance.encodings = {"e": encode_image(instance.image.url).tolist()}
        instance.save()


@receiver(post_delete, sender=ClassSet)
def class_deletw_handler(sender, **kwargs):
    instance = kwargs.get('instance')
    if os.path.exists(f"encodings/class{instance.id}.txt"):
        os.remove(f"encodings/class{instance.id}.txt")
