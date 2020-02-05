from rest_framework import viewsets
from rest_framework.response import Response

from scraper.models import Post
from scraper.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()[:10]

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
