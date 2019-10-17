from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from scraper.views import PostViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]
