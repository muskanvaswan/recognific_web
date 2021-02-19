![logo](https://raw.githubusercontent.com/muskanvaswan/recognific_web/master/base/static/Logo/Icon_recognific.ico)
# Recognific Website

## Introduction
Recognific is a user-friendly, web-based attendance model that makes the use of facial recognition.  In order to mark their attendance, the student simply has to look into the camera.

They would then get recognized by the model, based off the photos uploaded by the teacher- when they first initialize the class.

As the match gets confirmed, the time, as well as the name of the student will both get saved in a database which can be: queried, counted & manipulated by the teacher, and may even be converted into a downloadable excel-sheet.

## Features
1. Activate & deactivate auto generated distributable attendance link for students
2. Automated attendance sheet generation
3. Automatic calculation of percentage attendance per student, per class and more.
4. User friendly website with scalable database structures.

#### System Requirements for User
1. Have a good internet connection.
2. Use any of the following web browsers: Chrome, Mozilla or Safari.
3. Working webcam and sufficient lighting.
4. Permission to the website to access the webcam.

## Installation
After initializing a folder on your local system, execute the following:
[Make sure you have git CLI installed]
```bash
git clone https://github.com/muskanvaswan/recognific_web.git
```

Make a virtual environment, activate it, ensure that you are in your root directory and execute the following:
```bash
pip install -r requirements.txt
```
The file *requirements.txt* contains the dependencies for both the model and the website. *requirements1.txt* contains all the dependencies used for the face recognition model and *requiremnts2.txt* contains all the dependencies for the website itself.

## Structure of Codebase
All of the URLs for the website can be found in [URLS.md](https://github.com/muskanvaswan/recognific_web/blob/master/URLS.md)
#### The Base App (/base/)
**URL**: "\\"

This folder contains all the base functionality along with authentication and user models. This app also contains the base template and renders the home, about us and contact page.

**Models included**: User, Teacher

#### The Encode App (/encode/)
**URL**: "\\dashboard\\"

This folder contains all the functionality for interacting with different classes and students, i.e. creating, retrieving and deleting classes and students. This app also takes care of rendering the dashboard correctly. It also includes signals that connect these models to the recognize app, i.e. the Attendance model.

**Models included**: ClassSet, Student

#### The Recognize App (/recognize/)
**URL**: "\\r\\"

This folder contains the main functionality for the face recognition model, the VideoCamera object that is used in the streaming view along with functionality to mark the attendance correctly and update information in the respective ClassSet and Student model instances.

Kindly note, before you make changes to the models in this app, make sure you carefully understand its implications on the signal activity of the encode app.

**Models included**: Attendance


## Rebranding
To rebrand the website to your use case, ensure that you exchange the Recognific logo with your own.
Ensure that all the content on the contact page is suited to your institution.
Change the credentials for the email in **Recognific/setting.py**

```py
DEFAULT_FROM_EMAIL = 'YOUREMAIL@WHATEVER.COM'
EMAIL_HOST = 'smtp.gmail.com' # Change this to your email service provider
EMAIL_HOST_USER = 'YOUREMAIL@WHATEVER.COM'
EMAIL_HOST_PASSWORD = 'YOUR EMAIL APP PASSWORD'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

## Integrating your own database
You can integrate your own database to the website provided there is no clash in [database table names](https://github.com/muskanvaswan/recognific_web/blob/master/TABLES.md). You can do this by changing the following settings in *Recognific/settings.py*. Following the given example:
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ‘<db_name>’,
        'USER': '<db_username>',
        'PASSWORD': '<password>',
        'HOST': '<db_hostname_or_ip>',
        'PORT': '<db_port>',
    }
}
```

## Deployment
Before hosting, navigate to your folder on your command line interface and execute the following:
```bash
python manage.py check --deploy
```
This command will give you a checklist of things to do before deployment.

## References
[Repository for Model](https://github.com/muskanvaswan/recognific_model)<br>
[Opencv Documentation](https://docs.opencv.org/master/)<br>
[Face Recognition Model](https://pypi.org/project/face-recognition/)<br>
[Django documentation](https://docs.djangoproject.com/en/3.1/)
