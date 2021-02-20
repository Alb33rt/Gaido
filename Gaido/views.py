from django.shortcuts import render

from blog.models import Blogpost
from user_auth.models import User

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blogs(request):
    return render(request,'main/blog/blog.html')


def page_not_found(request, exception):
    data = {}
    return render(request, 'misc/404.html', data)
        