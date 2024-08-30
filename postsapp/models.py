from django.db import models
from userapp.models import User


class Post(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    def __str__(self):
        return self.title


class Comment(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.TextField()
    email = models.EmailField()
    body = models.TextField()
    def __str__(self):
        return self.name