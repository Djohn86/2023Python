from django.shortcuts import render, redirect
from .models import Sostav
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def index(request):
    player = Sostav.objects.all()
    return render(request, 'sostav/index.html', {'player': player})

# new


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'sostav/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                p1 = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                p1.save()
                login(request, p1)
                return redirect('addpost')

            except IntegrityError:
                return render(request, 'sostav/signup.html', {'form': UserCreationForm(),
                                                              'error': 'Такое имя пользователя существует. '
                                                                       'Создайте другое'})
        else:
            return render(request, 'sostav/signup.html', {'form': UserCreationForm(),
                                                          'error': 'Пароли не совпадают'})


def addpost(request):
    return render(request, 'sostav/addpost.html')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blogs')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'sostav/loginuser.html', {'form': AuthenticationForm()})
    else:
        p1 = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if p1 is None:
            return render(request, 'sostav/loginuser.html', {'form': AuthenticationForm(),
                                                             'error': 'Вы ввели неверные данные'})
        else:
            login(request, p1)
            return redirect('addpost')
