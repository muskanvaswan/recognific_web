from django.db import models
from django.contrib.auth.models import User
import numpy as np
import pickle


from .encodings import encode_image

# Create your models here.


class ClassSet(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ManyToManyField(User, blank=True)

    def make_encodings(self):
        IMAGES_LIST = [student.encodings for student in self.students.all()]
        ORDER_LIST = [student.id for student in self.students.all()]

        encodings = np.array(IMAGES_LIST)

        #encodings = np.array(list(map(encode_image, IMAGES_LIST)))
        encodings = {"encodings": encodings, "order": ORDER_LIST}

        # opening file in write mode (binary)
        file = open(f"encodings/class{self.id}.txt", "wb+")

        # serializing dictionary
        pickle.dump(encodings, file)
        # closing the file
        file.close()

    # def get_student_order(self):
        # return json.loads(self.student_order)

    def save(self, *args, **kwargs):
        self.make_encodings()
        return super().save(*args, **kwargs)


class Student(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80, default='')
    classname = models.ManyToManyField(ClassSet, related_name='students')
    image = models.ImageField(upload_to='images/students')
    encodings = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        for c in self.classname.all():
            c.make_encodings()
        self.encodings = encode_image(self.image.url)
        return super().save(*args, **kwargs)
