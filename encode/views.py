from django.views.generic.edit import CreateView
from .models import ClassSet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ClassSetCreateView(LoginRequiredMixin, CreateView):
    model = ClassSet
    success_url = reverse_lazy('index')
    fields = ['name', 'students', 'teacher']
    template_name = 'encode/make_classset.html'
