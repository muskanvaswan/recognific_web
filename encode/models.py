from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver

import numpy as np
import pickle
import json
import time

from .encodings import encode_image


def make_encodings(instance):
    c = instance
    print(c)
    IMAGES_LIST = [student.encodings['e'] for student in c.students.all()]
    ORDER_LIST = [student.id for student in c.students.all()]
    # print(ORDER_LIST)    # print(IMAGES_LIST)

    encodings = np.array(IMAGES_LIST)

    #encodings = np.array(list(map(encode_image, IMAGES_LIST)))
    encodings = {"encodings": encodings, "order": ORDER_LIST}
    # print("here")
    # opening file in write mode (binary)
    file = open(f"encodings/class{c.id}.txt", "wb+")

    # serializing dictionary
    pickle.dump(encodings, file)
    # closing the file
    file.close()


class Student(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80, default='')
    # classname = models.ManyToManyField(ClassSet, related_name='students')
    image = models.ImageField(upload_to='images/students')
    encodings = models.JSONField(blank=True, null=True)

    def save(self, *args, **kwargs):
        #self.encodings = {"e": encode_image(self.image.url).tolist()}
        return super().save(*args, **kwargs)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.get_full_name()}"


class ClassSet(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ManyToManyField(User, blank=True)
    students = models.ManyToManyField(Student, related_name='classname')

    def __str__(self):
        return f"{self.name} by {self.teacher}"


@receiver(post_save, sender=ClassSet)
def my_handler(sender, **kwargs):
    #print("on post save")
    # if kwargs.get('created') == True:
    # time.sleep(10)
    # kwargs.get("instance").save()

    print(kwargs.get("created"))
    make_encodings(kwargs.get("instance"))


@receiver(post_save, sender=Student)
def student_save_handler(sender, **kwargs):
    instance = kwargs.get('instance')
    if kwargs.get('created') == True:
        print("here")
        instance.encodings = {"e": encode_image(instance.image.url).tolist()}
        instance.save()

    # if kwargs.get("created"):
    # print(kwargs.get("instance"))
    # make_encodings(kwargs.get("instance"))
