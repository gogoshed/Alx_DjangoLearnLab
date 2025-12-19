from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create router and register the ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing list view
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for CRUD operations
    path('', include(router.urls)),
]
