from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from base.forms import SignUpForm
from django.urls import reverse_lazy


def index(request):
    print(request.user)
    return render(request, 'base/index.html')


## Authentication Functionality ##
def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # return render(request,'encode/dashboard.html')
            return redirect('/dashboard/')
        else:
            # Return an 'invalid login' error message.
            context = {"message": "Invalid Credentials"}
            return render(request, 'base/accounts/login.html', context)
    else:
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        else:
            return render(request, 'base/accounts/login.html')


def log_out_view(request):
    logout(request)
    return redirect('/accounts/login/')


def about(request):
    return render(request, 'base/about.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/dashboard")
        else:
            return redirect("/accounts/sign_up/")
    else:
        form = SignUpForm()
        return render(request, 'base/accounts/sign_up.html', {'form': form})
