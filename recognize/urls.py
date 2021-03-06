from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('cam/<str:classname>/', views.stream_view, name="camera"),
    path('face/<str:classname>/', views.face_view, name="face"),
    path('api/make_sheet/<int:classname>/', views.attendace_api, name="make_attendance")
]
