from django.shortcuts import render
from django.http import HttpResponse

from user_auth.models import User

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')