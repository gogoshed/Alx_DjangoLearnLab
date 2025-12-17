# blog/urls.py
# from django.urls import path
# from . import views
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
# )

# urlpatterns = [
#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('profile/', views.profile_view, name='profile'),
#     path('posts/', PostListView.as_view(), name='post-list'),
#     path('post/new/', PostCreateView.as_view(), name='post-create'),
#     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
#     path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
#     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
# ]




from django.urls import path
from . import views

from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    path('post/<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comments/', views.CommentListView.as_view(), name='comment_list'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),


    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),



]


