from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.form import LoginForm


# Create your views here.

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main:home')
            login_form.add_error(None, 'Invalid username or password.')
    else:
        if request.user.is_authenticated:
            return redirect('main:home')
        else:
            login_form = LoginForm()
    return render(request, 'main/login.html', {'login_form': login_form})


@login_required()
def main_view(request):
    return render(request, 'main/main.html')
