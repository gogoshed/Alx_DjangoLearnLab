from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='user-feed'),
]


from django.urls import path
from .views import like_post, unlike_post

urlpatterns = [
    path('<int:pk>/like/', like_post, name='like-post'),
    path('<int:pk>/unlike/', unlike_post, name='unlike-post'),
]


from django.urls import path
from .views import like_post, unlike_post

urlpatterns = [
    # ... your existing urls
    path('posts/<int:pk>/like/', like_post, name='like-post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post'),
]
