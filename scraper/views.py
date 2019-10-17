from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from scraper.models import Post
from scraper.serializers import PostSerializer
from scraper.services import ScraperManager


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=["get"])
    def scrape_websites(self, request):
        scraper_manager = ScraperManager()
        scraper_manager.run_requests()

        if True:
            return Response({"status": "password set"})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
