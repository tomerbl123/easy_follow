from django.db import models


class MediaUser(models.Model):
    username = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class Message(models.Model):
    content = models.CharField(max_length=255)
    media_user = models.ForeignKey(MediaUser, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class MediaUserFollow(models.Model):
    following_user = models.ForeignKey(MediaUser, on_delete=models.CASCADE, related_name='follower')
    followed_user = models.ForeignKey(MediaUser, on_delete=models.CASCADE, related_name='following')
    date_of_follow = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('following_user', 'followed_user',)
