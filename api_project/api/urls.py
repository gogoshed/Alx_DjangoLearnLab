from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define all URL patterns
urlpatterns = [
    # Simple list view
    path('books/', BookList.as_view(), name='book-list'),

    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Include all CRUD routes from the router
    path('', include(router.urls)),
]
