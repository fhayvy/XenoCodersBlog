from audioop import reverse
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from validate_email import validate_email
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from helpers.decorators import auth_user_should_not_access

# Create your views here.

# Home View
def home(request):
    return render(request, 'authentication/index.html')


# Log In View
def logout_user(request):

    logout(request)
    messages.success(request, 'Successfully Logged Out')

    return redirect(reverse('login'))


# Log Out View
@auth_user_should_not_access
def login_user(request):
    if request.method == "POST":
        context={'has_error': False, 'data':request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)

        if not user:
            messages.error(request, 'invalid credentials')
            return render(request, 'authentication/login.html', context)
        
        login(request, user)
        messages.success(request, f'Welcome {user.username}')

        return redirect(reverse('home'))

    return render(request, 'authentication/login.html')


# Register View
@auth_user_should_not_access
def register(request):
    if request.method == "POST":
        context={'has_error': False, 'data':request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password)<8:
            messages.error(request, 'Password is less than 8 characters')
            context['has_error'] = True
        
        if password != password2:
            messages.error(request, 'Password mismatch')
            context['has_error'] = True
        
        if not validate_email(email):
            messages.error(request, 'Enter a valid email address')
            context['has_error'] = True
        
        if not username:
            messages.error(request, 'Username is required')
            context['has_error'] = True
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is taken. Choose another one')
            context['has_error'] = True
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'There is already an account associated with this email.')
            context['has_error'] = True
        
        if context['has_error']:
            return render(request, 'authentication/register.html', context)
        
        user=User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'Account created. You can now Log In')

        return redirect('login')

    return render(request, 'authentication/register.html')