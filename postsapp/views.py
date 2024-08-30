from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):

        post_id = request.query_params.get("postId", None)
        if not post_id:
            return_comments = Comment.objects.all()
        else:
            return_comments = Comment.objects.filter(postId=post_id)
        serializer = self.get_serializer(return_comments, many=True)

        return Response(serializer.data)

