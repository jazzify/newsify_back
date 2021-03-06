from django.db import models
from common.models import BaseModel


class Post(BaseModel):

    TYPE_ETP = "ETP"
    TYPE_EPS = "EPS"
    TYPE_TWP = "TWP"

    TYPE_CHOICES = (
        (TYPE_ETP, "ELTIEMPO"),
        (TYPE_EPS, "ELPAIS"),
        (TYPE_TWP, "TWP"),
    )

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    author = models.CharField(max_length=50)
    body = models.TextField()
    cover_img_url = models.URLField(max_length=255, blank=True)
    original_post_url = models.URLField(max_length=512, unique=True)
    original_post_date = models.CharField(max_length=255)
    post_type = models.CharField(max_length=3, choices=TYPE_CHOICES)
