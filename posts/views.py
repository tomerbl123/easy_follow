from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status, mixins, generics

from . import models
from . import serializers


class CreateUserView(mixins.CreateModelMixin, generics.GenericAPIView):
    """
    Create a new Media User who can post messages or follow others' messages.
    """

    serializer_class = serializers.UserSerializer

    def post(self, request):
        return self.create(request)


class MessageView(APIView):
    """
    One can either post a new message for a specific user or fetch a feed of messages.
    The feed is either a private feed (according to the user's follows) or a global feed (all messages). Both feeds
    are ordered by the messages' creation date.
    """

    @staticmethod
    def get(request, **kwargs):
        if kwargs.get('media_user'):
            media_user = kwargs.get('media_user')
            follows = list(
                models.MediaUserFollow.objects.filter(following_user=media_user).values_list('followed_user', flat=True)
            )
            posts = models.Message.objects.filter(media_user__in=follows).order_by('-creation_date')
        else:
            posts = models.Message.objects.all().order_by('-creation_date')

        serializer = serializers.MessageSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    @staticmethod
    def post(request):
        new_message = JSONParser().parse(request)
        serializer = serializers.MessageSerializer(data=new_message)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowsHandleView(APIView):
    """
    Add a new follow or remove an existing one.
    """

    @staticmethod
    def post(request):
        new_follow = JSONParser().parse(request)
        serializer = serializers.MediaUsersFollowSerializer(data=new_follow)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        models.MediaUserFollow.objects.get(
            following_user=request.data['following_user'],
            followed_user=request.data['followed_user'],
        ).delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
