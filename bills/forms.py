from django import forms
from django.db import models

class NewBillForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    content = forms.CharField(label='Your message here', max_length=600, widget=forms.Textarea(attrs={'placeholder': 'Your message here'}) )
    author = forms.CharField(label='Author', max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Author'}))