import face_recognition as fr
import numpy as np
import cv2
import os
import sys
import datetime
from .reader import reading_encodings, csv_writter

IMAGES_LIST = os.listdir('images/creators/')
encodings = reading_encodings('creators')['encodings']


class VideoCamera(object):
    def __init__(self):
        self.webcam = cv2.VideoCapture(0)
        if not self.webcam.read(0)[0]:
            self.webcam = cv2.VideoCapture(1)

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
            matches = fr.face_distance(encodings, image)
            i = np.where(matches == min(matches))[0][0]
            name = IMAGES_LIST[i].split('.')[0]
            self.recognised.append(name)

        except:
            locations = (0, 0, 0, 0)
            name = ''

        frame = cv2.rectangle(frame, (locations[1], locations[0]),
                              (locations[3], locations[2]), (0, 255, 0), 2)
        frame = cv2.putText(frame, name,  (locations[3], locations[2]+20),
                            cv2.FONT_HERSHEY_SIMPLEX,  1, (0, 255, 0), 2, cv2.LINE_AA)

        res, jpeg = cv2.imencode('.jpeg', frame)

        return jpeg.tobytes()