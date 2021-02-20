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
            return HttpResponse('error')
    
    return render(request, 'login.html')

def signupview(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']

        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if password != confirmation:
            # Return Error message
            pass
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            # Return Error message
            pass
    
        login(request, user)
        return HttpResponseRedirect(reverse('main:index'))
    return render(request, 'sign-up.html')

@login_required(redirect_field_name='user_auth:login')
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))
