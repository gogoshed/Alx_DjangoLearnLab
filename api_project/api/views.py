from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# ListAPIView for listing books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ModelViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD operations on the Book model.
    Provides list, retrieve, create, update, and delete actions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
