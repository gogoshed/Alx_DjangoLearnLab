from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})
