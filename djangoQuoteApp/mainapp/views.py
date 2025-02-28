from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register_page(request):
    register_form = RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('index')
        
    return render(request, 'register.html', {
        'title': 'Register',
        'register_form': register_form
    })

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'You could not be authenticated')

    return render(request, 'login.html', {
        'title': 'Log In'
    })

def logout_user(request):
    logout(request)
    return redirect('index')