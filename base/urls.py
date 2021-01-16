from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('sign_up/', views.sign_up, name="sign_up"),
    path('about/', views.about, name="about")
]
#path('login/', auth_views.login, name="login"),
