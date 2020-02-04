from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from scraper.models import Post
from scraper.serializers import PostSerializer
from scraper.services import ScraperManager


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()[:10]
    serializer_class = PostSerializer

    @action(detail=False, methods=["get"])
    def scrape_websites(self, request):
        scraper_manager = ScraperManager()
        errors = scraper_manager.run_requests()

        if errors:
            return Response({"errors": errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status.HTTP_200_OK)
