from django.shortcuts import render, reverse
from django.contrib import messages

from Gaido.forms import SearchBarForm
from blog.models import Blogpost

from Gaido.utils import get_regions, get_categories

# Create your views here.
def index(request):
    posts = Blogpost.objects.all()
    featured_posts = Blogpost.objects.exclude(featured=False).all()
    return render(request, 'guidemain/full.html', {
        'searchform': SearchBarForm(),
        'categories': get_categories, 
        'regions': get_regions,
        'featured_posts': featured_posts,
        'posts': posts,
    })