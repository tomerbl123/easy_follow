from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaUser
        fields = ['id', 'username']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = ['id', 'content', 'media_user', 'creation_date']


class MediaUsersFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaUserFollow
        fields = ['id', 'following_user', 'followed_user']
