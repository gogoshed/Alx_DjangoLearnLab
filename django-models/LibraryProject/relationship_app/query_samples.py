from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Chinua Achebe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

print("Books by author:")
for book in books_by_author:
    print(book.title)


# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)  # <- use variable
library_books = library.books.all()

print("\nBooks in library:")
for book in library_books:
    print(book.title)


# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)

print("\nLibrarian for library:")
print(librarian.name)
