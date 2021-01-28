import face_recognition as fr
import numpy as np
import cv2
import os
import sys
import datetime
from .reader import reading_encodings, csv_writter
from encode.models import Student, ClassSet
from .models import Attendance


IMAGES_LIST = os.listdir('images/creators/')
encodings = reading_encodings('creators')['encodings']


class VideoCamera(object):
    def __init__(self, classname):
        self.webcam = cv2.VideoCapture(0)
        if not self.webcam.read(0)[0]:
            self.webcam = cv2.VideoCapture(1)
        self.classset = ClassSet.objects.get(pk=classname.split('class')[1])
        data = reading_encodings(classname)
        if data['order'] == []:
            self.classset.save()
            data = reading_encodings(classname)

        self.IMAGES_LIST = [Student.objects.get(pk=id) for id in data['order']]

        #self.IMAGES_LIST = os.listdir(f'images/{classname}/')
        self.encodings = data['encodings']

        self.recognised = []

    def __del__(self):
        self.webcam.release()

    def detect(self):

        status, frame = self.webcam.read()

        scale = 45
        width = int(frame.shape[1] * scale / 100)
        height = int(frame.shape[0] * scale / 100)
        dim = (width, height)

        # resize image
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

        try:
            locations = fr.face_locations(frame)
            locations = locations[0]

            image = fr.face_encodings(frame)[0]
            matches = fr.face_distance(self.encodings, image)
            i = np.where(matches == min(matches))[0][0]
            name = self.IMAGES_LIST[i].user.get_full_name()
            self.recognised.append(self.IMAGES_LIST[i])

        except:
            locations = (0, 0, 0, 0)
            name = ''

        frame = cv2.rectangle(frame, (locations[1], locations[0]),
                              (locations[3], locations[2]), (0, 255, 0), 2)
        frame = cv2.putText(frame, name,  (locations[3], locations[2]+20),
                            cv2.FONT_HERSHEY_SIMPLEX,  0.5, (0, 255, 0), 1, cv2.LINE_AA)

        res, jpeg = cv2.imencode('.jpeg', frame)

        return jpeg.tobytes()

    def attendace(self):
        person = max(self.recognised, key=self.recognised.count)
        a = Attendance(classname=self.classset, student=person)
        a.save()
        img = fr.load_image_file("images/checkmark.gif")
        img = cv2.putText(img, "Attendance marked for "+person.user.get_full_name(),  (35, 290),
                          cv2.FONT_HERSHEY_SIMPLEX,  0.5, (0, 0, 0), 1, cv2.LINE_AA)
        res, jpeg = cv2.imencode('.jpeg', img)
        return (jpeg.tobytes(), a.id)
        # attendance = [person.get_full_name(), str(datetime.datetime.now())]
        # csv_writter(attendance)
