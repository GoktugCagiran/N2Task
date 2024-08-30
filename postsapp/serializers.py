from rest_framework import serializers
from .models import Post, Comment
from userapp.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["userId", "id", "title", "body"]

    # def validate_userId(self, value):
    #     if not User.objects.filter(id=value.id).exists():
    #         raise serializers.ValidationError("User does not exist")
    #     return value


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["postId", "id", "name", "email", "body"]

    # def validate_postId(self, value):
    #     print("Comment Validate postId: ", value)
    #     if not Post.objects.filter(id=value.id).exists():
    #         raise serializers.ValidationError("Post doesn't exist")
        
    #     return value