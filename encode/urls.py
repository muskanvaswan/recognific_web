from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClassSetCreateView.as_view(), name="create_classset"),
]
