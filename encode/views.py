from django.views.generic.edit import CreateView, TemplateView
from .models import ClassSet, Student
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ClassSetCreateView(LoginRequiredMixin, CreateView):
    model = ClassSet
    success_url = reverse_lazy('index')
    fields = ['name', 'students', 'teacher']
    template_name = 'encode/create.html'


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    success_url = reverse_lazy('index')
    fields = ['first_name', 'last_name', 'image']
    template_name = 'encode/create.html'


class DashboardView(TemplateView):
    template_name = 'encode/dashboard.html'
