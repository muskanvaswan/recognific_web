from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'base/index.html')


def sign_in(request):
    return render(request, 'base/login.html')


def sign_up(request):
    return render(request, 'base/sign_up.html')
