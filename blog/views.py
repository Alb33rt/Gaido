import uuid as a

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.core.exceptions import PermissionDenied

from user_auth.models import User

from .forms import CreatePostForm
from .models import Blogpost
# Create your views here.
def index(request):
    posts = Blogpost.objects.all()
    featured_posts = Blogpost.objects.exclude(featured=False).all()

    for features in featured_posts:
        if features.thumbnail:
            imageurl = features.thumbnail.url
        
        else:
            imageurl = False
        print(imageurl)
    return render(request, 'blog/index.html', {
        'posts': posts,
        'featured_posts': featured_posts,
        'user': request.user,
    })

def createPost(request):
    if not request.user.has_perm('blog.add_blogpost'):
        return HttpResponseRedirect(reverse('main:no_perm'))
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        content = form['content']
        if form.is_valid():
            title = form.cleaned_data.get('title')
            briefing = form.cleaned_data.get('briefing')

            thumbnail = form.cleaned_data.get('thumbnail')

            category = form.cleaned_data.get('category')
            region = form.cleaned_data.get('region')

            uuid = a.uuid4()

            f = Blogpost(uuid=uuid, title=title, briefing=briefing, content=content, author=request.user, thumbnail=thumbnail)
            f.save()

            print(f)

            if f is None:
                return HttpResponse('error')

            return HttpResponseRedirect(reverse('blog:index'))
    
    else:
        form = CreatePostForm(initial={
            'region': 'Kanto',
            'category': 'General',
        })
        return render(request, 'blog/create.html', {
            'form': form,
        })

def blogpost(request, uuid):
    post = Blogpost.objects.filter(uuid=uuid).get()
    return render(request, 'blog/blogpost.html', {
        'post': post,
    })
