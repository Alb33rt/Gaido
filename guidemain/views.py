from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


from Gaido.forms import SearchBarForm
from blog.models import Blogpost, Type, Region

from Gaido.utils import get_regions, get_categories

from .utils import find_match_specific

# Create your views here.
def index(request):
    posts = Blogpost.objects.all()
    region_posts = Blogpost.objects.all()
    best_posts = Blogpost.objects.filter(must_view=True).all()
    featured_posts = Blogpost.objects.exclude(featured=False).all()
    return render(request, 'guidemain/full.html', {
        'searchform': SearchBarForm(),
        'categories': get_categories, 
        'regions': get_regions,
        'featured_posts': featured_posts,
        'posts': posts,
        'bests': best_posts,
    })

def specficview(request):
    query = request.GET.get('sortby')
    match_lst = find_match_specific(query)
    match = match_lst[0]

    cat_posts = Blogpost.objects.filter(category=match).all()
    reg_posts = Blogpost.objects.filter(region=match).all()

    if cat_posts:
        posts = cat_posts
    elif reg_posts:
        posts = reg_posts
    else:
        return render(request, 'misc/404.html')
        
    return render(request, 'guidemain/specific.html', {
        'searchform': SearchBarForm(),
        'categories': get_categories,
        'regions': get_regions,
        'posts': posts,
        'category': query,
    })