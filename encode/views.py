from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from .models import ClassSet, Student
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect


class ClassSetCreateView(LoginRequiredMixin, CreateView):
    model = ClassSet
    success_url = reverse_lazy('dashboard')
    fields = ['name', 'students', 'teacher']
    template_name = 'encode/create.html'


class ClassSetUpdateView(LoginRequiredMixin, UpdateView):
    model = ClassSet
    success_url = reverse_lazy('dashboard')
    fields = ['name', 'students', 'teacher']
    template_name = 'encode/update.html'


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
    fields = ['user', 'image']
    template_name = 'encode/create.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'encode/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = self.request.user.classes.all()
        attendance = []
        try:
            for classname in self.request.user.student.classname.all():
                class_attendance = {
                    "classname": classname.name,
                    "attended": self.request.user.student.attendance.filter(classname=classname).count(),
                    "total": classname.occourance
                }
                attendance.append(class_attendance)
                context['attendance'] = attendance
        except:
            pass
        return context


def activate_class_set(request, classset_id):
    ClassSetObject = ClassSet.objects.get(pk=classset_id)
    ClassSetObject.activate()
    return redirect('/dashboard')


def deactivate_class_set(request, classset_id):
    ClassSetObject = ClassSet.objects.get(pk=classset_id)
    ClassSetObject.deactivate()
    return redirect('/dashboard')
