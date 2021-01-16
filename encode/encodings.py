import face_recognition as fr
import numpy as np
import pickle


def encode_image(path):
    path = path[1:]
    img = fr.load_image_file(f"{path}")
    try:
        return fr.face_encodings(img)[0]
    except:
        pass


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
