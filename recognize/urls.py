from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.stream_view, name="camera"),
    path('face/', views.face_view, name="face")
]
