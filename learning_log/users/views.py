from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import UserLogin, UserRegister


def user_login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return redirect('/topics/')
    else:
        form = UserLogin()
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('learning_logs:index')


def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect('/topics/')
    else:
        form = UserRegister()
    
    return render(request, 'users/register.html', {'form': form})
