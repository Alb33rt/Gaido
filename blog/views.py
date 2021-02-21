import uuid as a

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.core.exceptions import PermissionDenied

from user_auth.models import User

from .forms import CreatePostForm, EditPostForm
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

def authorperm(user):
    if not user.has_perm('blog:add_blogpost'):
        return HttpResponseRedirect(reverse('main:no_perm'))
    else:
        pass

def createPost(request):
    authorperm(request.user)
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Context
            title = form.cleaned_data.get('title')
            briefing = form.cleaned_data.get('briefing')
            content = form.cleaned_data['content']
            thumbnail = form.cleaned_data['thumbnail']
            category = form.cleaned_data['category']
            region = form.cleaned_data['region']
            uuid = a.uuid4()

            f = Blogpost(uuid=uuid, title=title, briefing=briefing, content=content, author=request.user, thumbnail=thumbnail, category=category, region=region)
            f.save()

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

def editpost(request, uuid):
    authorperm(request.user)

    if request.method == "POST":
        # code that updates the blogpost
        pass

    post = Blogpost.objects.filter(uuid=uuid).get()
    form = EditPostForm(initial={
        'title': post.title,
        'content': post.content,
        'briefing': post.briefing,
        'category': post.category,
        'region': post.region,
    })

    return render(request, 'blog/edit.html', {
        'form': form,
    })
