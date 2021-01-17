from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('classset/create/', views.ClassSetCreateView.as_view(), name="create_classset"),
    path('student/create/', views.StudentCreateView.as_view(), name="create_student"),

]
