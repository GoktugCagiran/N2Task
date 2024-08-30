from rest_framework import serializers
from .models import Album, Photo


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["userId", "id", "title"]


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["albumId", "id", "title", "url", "thumbnailUrl"]