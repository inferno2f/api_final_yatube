from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import CommentSerializer, PostSerializer
from .permissions import IsOwnerOrReadOnly
from posts.models import Post, Comment, Group, Follow


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def _get_post(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self._get_post())
    
    def get_queryset(self):
        queryset = Comment.objects.filter(post=self._get_post())
        return queryset