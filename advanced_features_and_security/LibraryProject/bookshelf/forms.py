from django import forms
from .models import Book

# Example form to create/edit Book instances
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
