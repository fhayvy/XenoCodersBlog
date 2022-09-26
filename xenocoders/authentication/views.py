from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from validate_email import validate_email
from .models import User
# Create your views here.

def home(request):
    return render(request, 'authentication/index.html')

def login(request):
    return render(request, 'authentication/login.html')

def register(request):
    if request.method == "POST":
        context={'has_error': False}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password)<8:
            messages.add_message(request,messages.ERROR, 'Password is less than 8 characters')
            context['has_error'] = True
        
        if password != password2:
            messages.add_message(request,messages.ERROR, 'Password mismatch')
            context['has_error'] = True
        
        if not validate_email(email):
            messages.add_message(request,messages.ERROR, 'Enter a valid email address')
            context['has_error'] = True
        
        if not username:
            messages.add_message(request,messages.ERROR, 'Username is required')
            context['has_error'] = True
        
        if User.objects.filter(username=username).exists():
            messages.add_message(request,messages.ERROR, 'Username is taken. Choose another one')
            context['has_error'] = True

    return render(request, 'authentication/register.html')