from django.shortcuts import render, get_object_or_404

from blog.models import Blogpost
from user_auth.models import User

from .forms import SearchBarForm

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def perm_denied(request):
    return render(request, 'misc/perm_denied.html')


def page_not_found(request, exception):
    data = {}
    return render(request, 'misc/404.html', data)

def search(request):
    form = SearchBarForm(request.GET)
    if form.is_valid:
        results = form.cleaned_data.get('search')



        