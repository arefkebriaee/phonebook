from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterFrom, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login(request):

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            passw = form.cleaned_data['password']
            user = authenticate(request, username=name, password=passw)
            if user is not None:
                login(request, user)
                messages.success(request, "you logged in successfuly!")
                return redirect('contact:home')
            else:
                messages.error(
                    request, "your username or password is incorrect!!!")
    else:
        form = LoginUserForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterFrom, LoginUserForm
        if form.is_valid():
            clean_data = form.cleaned_data
            User.objects.create_user(
                clean_data['username'], clean_data['password'])
            messages.success(request, "you are registered successfully")
            return redirect('accounts:user_login')
        else:
            messages.warning(request, 'you input invalid data!!!')
    else:
        form = UserRegisterFrom
    return render(request, 'accounts/register.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, "you logged out succesfully")
    return redirect('contact:home')
