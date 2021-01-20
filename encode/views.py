from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import ClassSet, Student
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ClassSetCreateView(LoginRequiredMixin, CreateView):
    model = ClassSet
    success_url = reverse_lazy('index')
    fields = ['name', 'students', 'teacher']
    template_name = 'encode/create.html'


class ClassSetDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'encode/classset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('classset_id')
        object = ClassSet.objects.get(pk=id)
        context['classset'] = object
        context['attendance'] = object.attendees.all()[:10][::-1]
        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    success_url = reverse_lazy('index')
    fields = ['first_name', 'last_name', 'image']
    template_name = 'encode/create.html'


class DashboardView(TemplateView):
    template_name = 'encode/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = self.request.user.classes.all()
        return context
