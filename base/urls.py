from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/login/', views.sign_in, name="login"),
    path('accounts/logout/', views.log_out_view, name="logout"),
    path('accounts/sign_up/', views.sign_up, name="sign_up"),
    path('accounts/sign_up_as/', views.sign_up_as, name="sign_up_as"),
    path('accounts/user/<pk>', views.UserUpdateView.as_view(), name="user_update"),
    path('about/', views.about, name="about"),
    path('contact/', views.ContactView.as_view(), name="contact")

]
