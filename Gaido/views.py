import html2text

from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

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
    response = render_to_response('misc/500.html', {}, context_instance = RequestContext(request))
    response.status_code = 500
    return response


def search(request):
    if request.method == "POST":
        form = SearchBarForm(request.POST)
        if form.is_valid():
            # Context
            query = request.POST['search']
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

            return render(request, 'main/searchresults.html', {
                'primaryresults': posts,
                'secondaryresults': body_posts,
                'categories': get_categories,
                'regions': get_regions,
                'searchform': SearchBarForm
            })
    else:
        return render(request, 'misc/404.html')
