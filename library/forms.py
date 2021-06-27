from django import forms

# from django.contrib.auth.models import User
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'isbn', 'author', 'publisher']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'pid', 'email', 'address']


class IssuedBookForm(forms.ModelForm):
    expires_on = forms.DateField(required=False)

    class Meta:
        model = Issued
        fields = ['isbn', 'pid', 'expires_on']
