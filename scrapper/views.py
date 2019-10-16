from django.shortcuts import render
from rest_framework import viewsets

from scrapper.models import Post
from scrapper.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
