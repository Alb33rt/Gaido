from django import forms
from django.forms import TextInput, SelectMultiple
from tinymce.widgets import TinyMCE

from .models import Blogpost

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'content', 'region', 'category']

        labels= {
            'title': ('Title of Post')
        }
        widgets = {
            'title': TextInput(attrs={'class': "form-control", 'size': 40, 'placeholder': "Enter the Title"}),
            'content': TinyMCE(attrs={'class': "form-control", 'cols': 80, 'rows': 60}),
            'region': SelectMultiple(attrs={'class': "form-control"}),
            'category':  SelectMultiple(attrs={'class': "form-control"}),
        }