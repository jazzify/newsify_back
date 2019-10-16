from django.db import models
from common.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=50)
    body = models.TextField()
    cover_img_url = models.URLField(max_length=255, blank=True)
    original_post_url = models.URLField(max_length=512)
