from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm

# Create your views here.
def home(request):
    context = {
        'user': request.user
    }
    return render(request, 'index.html', context)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('login')
