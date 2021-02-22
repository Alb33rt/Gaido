from django import forms
from django.forms import ModelForm


# Define the forms here
class SearchBarForm(forms.Form):
    search = forms.CharField(
        max_length=32,
        widget=forms.TextInput(
            attrs={'class': 'form-control ml-2', 'placeholder': 'Search in Gaido...'}
            )
        )