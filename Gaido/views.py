from django.shortcuts import render

from blog.models import Blogpost

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blogs(request):
    return render(request,'main/blog/blog.html')