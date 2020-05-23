from accounts.forms import UserRegisterForm, UserLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages


def register(request):
    """ Реєстрація нових користувачів """

    context = {}
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Реєстрація пройшла успішно!')
            return redirect('news:index-page')
        else:
            messages.error(request, 'Помилка реєстрації')
    else:
        form = UserRegisterForm()
    context['form'] = form

    return render(request, 'accounts/register.html', context)


def user_login(request):
    """ Авторизація користувачів """

    context = {}

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('news:index-page')
    else: 
        form = UserLoginForm()

    context['form'] = form

    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('news:index-page')