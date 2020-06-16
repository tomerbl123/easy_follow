from django.contrib import admin
from . import models


class MediaUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    ordering = ['id']


class MessageAdmin(admin.ModelAdmin):
    list_display = ['media_user', 'content', 'creation_date']
    list_select_related = ['mediauser__username']
    ordering = ['id']


class MediaUserFollowAdmin(admin.ModelAdmin):
    list_display = ['id', 'following_user', 'followed_user']
    list_select_related = ['following_user', 'followed_user']
    ordering = ['id']


admin.site.register(models.MediaUser, MediaUserAdmin)
admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.MediaUserFollow, MediaUserFollowAdmin)
