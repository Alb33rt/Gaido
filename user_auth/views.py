from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import User

# Create your views here.
def loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        print(user)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
        else:
            # Use the Django messages framework to provide message for failed
            message = "Login Failed. You may have entered incorrect username or password."
            messages.error(request, message)
            return HttpResponseRedirect(reverse('user_auth:login'))
    
    return render(request, 'login.html')

def signupview(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']

        password = request.POST['password']
        confirmation = request.POST['confirmation']
    
        try: 
            terms = request.POST['terms']
        except:
            terms = False
        
        if password != confirmation:
            # Return Error message
            message = "Sorry, the confirmation password you entered was different from the password you entered."
            messages.error(request, message)
            return HttpResponseRedirect(reverse('user_auth:signup'))

        if terms == False:
            # Return Please accept message
            message = "You did not agree to the terms and services."
            messages.error(request, message)
            return HttpResponseRedirect(reverse('user_auth:signup'))
        
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            message = "This message has been used before."
            messages.error(request, message)
            return HttpResponseRedirect(reverse('user_auth:signup'))
    
        login(request, user)
        return HttpResponseRedirect(reverse('main:index'))
    return render(request, 'sign-up.html')

@login_required(redirect_field_name='user_auth:login')
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))
