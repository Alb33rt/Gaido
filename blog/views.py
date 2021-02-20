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
    return render(request, 'blog/index.html', {
        'user': request.user
    })

def createPost(request):
    if not request.user.has_perm('blog.add_blogpost'):
        return HttpResponse('Permission Denied')
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        title = form['title']
        content = form['content']

        category = form['category']
        region = form['region']

        uuid = a.uuid4()

        f = Blogpost(uuid=uuid, title=title, content=content, author=request.user)
        f.save()

        print(f)

        if f is None:
            return HttpResponse('error')

        return HttpResponseRedirect(reverse('blog:index'))
    
    else:
        return render(request, 'blog/create.html', {
            'form': CreatePostForm(),
        })