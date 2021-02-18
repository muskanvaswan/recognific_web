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

## Installation
After initializing a folder on your local system, execute the following:
[Make sure you have git CLI installed]
```bash
git clone https://github.com/muskanvaswan/recognific_web.git
```
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

## Deployment
Before hosting, navigate to your folder on your command line interface and execute the following:
```bash
python manage.py check --deploy
```
This command will give you a checklist of things to do before deployment.

## 
