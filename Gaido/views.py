import html2text

from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator

from blog.models import Blogpost, Type, Region
from user_auth.models import User

from .forms import SearchBarForm
from .utils import get_categories, get_regions

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {
        'categories': get_categories,
        'regions': get_regions,
        'searchform': SearchBarForm()
    })

def support(request):
    return render(request, 'main/support.html', {
        'categories': get_categories,
        'regions': get_regions,
        'searchform': SearchBarForm(),
    })

def perm_denied(request):
    return render(request, 'misc/perm_denied.html', {
        'categories': get_categories,
        'regions': get_regions,
        'searchform': SearchBarForm,
    })


def page_not_found(request, exception):
    response = render_to_response('misc/404.html', {}, context_instance = RequestContext(request))
    response.status_code = 404
    return response

def server_error(request):
    response = render(request, 'misc/500.html')
    response.status_code = 500
    return response


def search(request):
    # Context
    query = request.GET.get('search')
    query = query.strip().lower()
    body_posts = []
    
    # Search body algo 
    allposts = Blogpost.objects.all()
    for post in allposts:
        content_in_string = html2text.html2text(post.content)
        if query in content_in_string:
            body_posts.append(post)
        else: 
            pass

        
    posts = Blogpost.objects.filter(title__icontains=query, briefing__icontains=query).all()

    p = Paginator(posts, 10)
    p2 = Paginator(body_posts, 10)

    if request.GET.get('page'):
        page_number = request.GET.get('page')
    else:
        page_number = 1
    
    all_page_obj = p.page(page_number)
    body_page_obj = p2.page(page_number)

    if len(body_page_obj) > len(all_page_obj):
        page_obj = body_page_obj
    else:
        page_obj = all_page_obj

    print(len(all_page_obj))
    print(len(body_page_obj))

    return render(request, 'main/searchresults.html', {
        'all_page_obj': all_page_obj,
        'body_page_obj': body_page_obj,
        'page_obj': page_obj,
        'query': query,
        'categories': get_categories,
        'regions': get_regions,
        'searchform': SearchBarForm
    })

