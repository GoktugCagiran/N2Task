from django.db import models
from userapp.models import User


class Todo(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    completed = models.BooleanField()
