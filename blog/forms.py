from django import forms
from django.forms import TextInput, SelectMultiple, Textarea, Select, URLInput, FileInput
from tinymce.widgets import TinyMCE

from .models import Blogpost, Comment

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'briefing', 'content', 'thumbnail', 'region', 'category', 'related_posts']

        labels= {
            'title': ('Title of Post'),
            'related_posts': ('Links to other posts'),
        }
        
        widgets = {
            'title': TextInput(attrs={'class': "form-control", 'size': 40, 'placeholder': "Enter the Title..."}),
            'briefing': Textarea(attrs={'class': "form-control", 'placeholder': "Enter the briefing..."}),
            'thumbnail': FileInput(attrs={'class': 'form-control', 'required': True}),
            'region': Select(attrs={'class': "form-control",}, ),
            'category':  Select(attrs={'class': "form-control",}, ),
            'related_posts': Select(attrs={'class': 'form-control', 'placeholder': "Insert Post..."}),
        }

class EditPostForm(CreatePostForm):
    thumbnail = forms.ImageField(disabled= True)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]

        widgets = {
            'content': TextInput(attrs={'class': 'form-control', 'row': 2})
        }