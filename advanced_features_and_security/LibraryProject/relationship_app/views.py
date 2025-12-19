from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # Make sure you have a ModelForm for Book
from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import render

# ----------------------
# Add Book
# ----------------------
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

# ----------------------
# Edit Book
# ----------------------
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

# ----------------------
# Delete Book
# ----------------------
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})





# Check if user is an admin
def is_admin(user):
    return user.is_superuser or (hasattr(user, 'userprofile') and user.userprofile.role == 'Admin')

@user_passes_test(is_admin)
def admin_view(request):
    # Example: list all books
    from .models import Book
    books = Book.objects.all()
    return render(request, 'relationship_app/admin_view.html', {'books': books})





def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    # Example: list books in the librarian's library
    from .models import Library
    try:
        library = request.user.userprofile.library  # optional: if you link userprofile to Library
        books = library.books.all()
    except AttributeError:
        books = []
    return render(request, 'relationship_app/librarian_view.html', {'books': books})





def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    # Example: list all books
    books = Book.objects.all()
    return render(request, 'relationship_app/member_view.html', {'books': books})




def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'








def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'relationship_app/list_books.html', {'books': books})


from django.views.generic.detail import DetailView
from .models import Library  # Make sure you have a Library model

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Your template path
    context_object_name = 'library'  # Optional, for template usage


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')  # Make sure you have a login URL
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'


from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def add_book(request):
    # your code to add a book (form handling)
    pass

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # your code to edit the book (form handling)
    pass

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # your code to delete the book
    pass



from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm  # assuming you have a form for Book

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})


from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
