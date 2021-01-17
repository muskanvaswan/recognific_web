from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="base/accounts/login.html"),name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name="base/accounts/logout.html"),name="logout"),
    path('accounts/sign_up/', views.sign_up, name="sign_up"),
    path('about/', views.about, name="about")
]
