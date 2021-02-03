from django import forms
from django.forms import ModelForm
#from django.contrib.auth.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.core.mail import send_mail
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


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ContactForm(forms.Form):
    full_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    def send_email(self):
        full_name = self.cleaned_data.get('full_name')
        message = self.cleaned_data.get('message')
        email = self.cleaned_data.get('email')
        send_mail(
            subject=f"Contact from CSI website by {full_name}",
            message=f"{message} from {email}",
            from_email='csi.bennett19@gmail.com',
            recipient_list=['muskanvaswan2@gmail.com'],
            fail_silently=False,
        )
