from django import forms
from django.forms import ModelForm


# Define the forms here
class SearchBarForm(forms.Form):
    search = forms.CharField(max_length=32)