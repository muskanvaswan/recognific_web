from django import forms
from django.forms import ModelForm
#from django.contrib.auth.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from encode.models import Student
#
#
# class StudentCreateForm(forms.ModelForm):
# class Meta:
# model = Student


class UserCreateForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
