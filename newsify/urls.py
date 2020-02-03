from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from scraper.views import PostViewSet

router = routers.DefaultRouter()
router.register(r"api/posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]
# Docs
urlpatterns += [
    path('openapi/', get_schema_view(
        title="Newsify",
        version="0.1.0"
    ), name='openapi-schema'),
    path('api-docs/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
