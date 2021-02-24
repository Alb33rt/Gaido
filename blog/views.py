import uuid as a

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.core.exceptions import PermissionDenied

from user_auth.models import User
from Gaido.forms import SearchBarForm
from Gaido.utils import get_regions, get_categories

from .forms import CreatePostForm, EditPostForm, CommentForm
from .models import Blogpost, Comment
# Create your views here.
def index(request):
    posts = Blogpost.objects.all()
    featured_posts = Blogpost.objects.exclude(featured=False).all()
    p = Paginator(posts, 7)
    
    if request.GET.get('page'):
        page_number = request.GET.get('page')
    else:
        page_number = 1

    page_obj = p.page(page_number)

    for features in featured_posts:
        print(features.category)
        if features.thumbnail:
            imageurl = features.thumbnail.url
        
        else:
            imageurl = False
        print(imageurl)

    return render(request, 'blog/index.html', {
        'featured_posts': featured_posts,
        'page_obj': page_obj,
        'categories': get_categories,
        'regions': get_regions,
        'searchform': SearchBarForm(),
    })

def authorperm(user):
    if not user.has_perm('blog:add_blogpost'):
        return HttpResponseRedirect(reverse('main:no_perm'))
    else:
        pass

def createPost(request):
    authorperm(request.user)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:no_perm'))
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
                return render(request, 'misc/500.html')

            return HttpResponseRedirect(reverse('blog:index'))
    
    else:
        form = CreatePostForm(initial={
            'region': 'Kanto',
            'category': 'General',
        })
        return render(request, 'blog/create.html', {
            'form': form,
            'categories': get_categories,
            'regions': get_regions,
            'searchform': SearchBarForm(),
        })

def blogpost(request, uuid):
    post = Blogpost.objects.filter(uuid=uuid).get()
    comments = Comment.objects.filter(post=post).all()

    author = post.author
    authorobject = User.objects.filter(username=author).first()
    return render(request, 'blog/blogpost.html', {
        'post': post,
        'categories': get_categories,
        'regions': get_regions,
        'searchform': SearchBarForm(),
        'author': authorobject,
        'commentform': CommentForm(),
        'comments': comments,
    })

def editpost(request, uuid):
    authorperm(request.user)

    if request.method == "POST":
        if uuid:
            post = get_object_or_404(Blogpost, uuid=uuid)
            if request.user != post.author:
                return render(request, 'misc/perm_denied.html')
            else: 
                pass
        
        # code that updates the blogpost
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            briefing = form.cleaned_data.get('briefing')
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            region = form.cleaned_data['region']

            form.save(commit=True)
            return HttpResponseRedirect(reverse('blog:blogpost', args=[uuid]))
            
        else:
            return render(request, 'misc/500.html')

    
    post = Blogpost.objects.filter(uuid=uuid).get()
    if post.related_posts:
        form = CreatePostForm(initial={
            'title': post.title,
            'content': post.content,
            'briefing': post.briefing,
            'category': post.category,
            'region': post.region,
            'related_posts': post.related_posts,
        })
    else:
        form = CreatePostForm(initial={
            'title': post.title,
            'content': post.content,
            'briefing': post.briefing,
            'category': post.category,
            'region': post.region,
        })

    print(uuid)

    return render(request, 'blog/edit.html', {
        'form': form,
        'categories': get_categories,
        'regions': get_regions,
        'searchform': SearchBarForm(),
        'uuid': post.uuid
    })


def comment(request, uuid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            user = request.user
            post = Blogpost.objects.filter(uuid=uuid).get()

            if (content.strip() == ""):
                message = "Please do not enter empty in comments."
                messages.error = (request, message)
                return HttpResponseRedirect(reverse('blog:blogpost', args=[uuid]))
            
            newcomment = Comment(user=user, content=content, post=post)
            newcomment.save()

            return HttpResponseRedirect(reverse('blog:blogpost', args=[uuid]))
    else:
        return render(request, 'misc/500.html')