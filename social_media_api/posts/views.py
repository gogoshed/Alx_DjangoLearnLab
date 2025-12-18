from django.shortcuts import render

from rest_framework import viewsets, permissions, filters, generics
from rest_framework.pagination import PageNumberPagination

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = Post.objects.filter(pk=pk).first()
    if not post:
        return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return Response({"detail": "Already liked."}, status=status.HTTP_400_BAD_REQUEST)

    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )
    return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = Post.objects.filter(pk=pk).first()
    if not post:
        return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)
    like = Like.objects.filter(user=request.user, post=post).first()
    if like:
        like.delete()
        return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
    return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404

from .models import Post, Like
from notifications.models import Notification  # if you want to create notifications


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    """
    Like a post. If already liked, do nothing.
    """
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # Check if user already liked the post
    if Like.objects.filter(post=post, user=user).exists():
        return Response({'detail': 'Already liked.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create the like
    Like.objects.create(post=post, user=user)

    # Optional: create a notification
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='liked',
        target=post
    )

    return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    """
    Unlike a post. If not liked, return an error.
    """
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    like = Like.objects.filter(post=post, user=user).first()
    if not like:
        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    like.delete()
    return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)



post = generics.get_object_or_404(Post, pk=pk)



@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    user = request.user

    if Like.objects.filter(post=post, user=user).exists():
        return Response({'detail': 'Already liked.'}, status=status.HTTP_400_BAD_REQUEST)

    Like.objects.create(post=post, user=user)

    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='liked',
        target=post
    )

    return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    user = request.user

    like = Like.objects.filter(post=post, user=user).first()
    if not like:
        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    like.delete()
    return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
