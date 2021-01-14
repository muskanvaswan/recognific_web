import face_recognition as fr


def encode_image(path):
    path = path[1:]
    img = fr.load_image_file(f"{path}")
    try:
        return fr.face_encodings(img)[0]
    except:
        pass
