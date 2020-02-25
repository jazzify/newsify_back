from rest_framework import viewsets, mixins
from rest_framework.response import Response

from scraper.models import Post
from scraper.serializers import PostSerializer


class PostViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        post_types = [post_type[0] for post_type in Post.TYPE_CHOICES]
        posts = {post_type:[] for post_type in post_types}

        for post_type in post_types:
            queryset = Post.objects.filter(post_type=post_type).order_by('-created_at')[:4]
            serialized_posts = self.get_serializer(queryset, many=True).data
            posts[post_type] = serialized_posts
        
        return Response(posts)
