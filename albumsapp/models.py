from django.db import models
from userapp.models import User


class Album(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()


class Photo(models.Model):
    albumId = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.TextField()
    url = models.URLField()
    thumbnailUrl = models.URLField()