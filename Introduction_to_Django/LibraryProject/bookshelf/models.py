from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


from django.contrib import admin
from .models import Book

# Register Book model with admin using ModelAdmin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # shows these fields in admin list view
    list_filter = ('author', 'publication_year')            # enables filter sidebar
    search_fields = ('title', 'author')                     # enables search box

admin.site.register(Book, BookAdmin)
