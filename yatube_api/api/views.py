# TODO:  Напишите свой вариант
from rest_framework import viewsets

from .serializers import PostSerializer
from posts.models import Post, Comment, Group, Follow


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer