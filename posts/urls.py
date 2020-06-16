from django.urls import path

from . import views


app_name = 'posts'
urlpatterns = [
    path('create_user/', views.CreateUserView.as_view(), name='create_user_view'),
    path('post_message/', views.MessageView.as_view(), name='post_message'),
    path('follow/', views.FollowsHandleView.as_view(), name='follow'),
    path('unfollow/', views.FollowsHandleView.as_view(), name='unfollow'),
    path('get_feed/<int:media_user>/', views.MessageView.as_view(), name='get_feed'),
    path('get_global_feed/', views.MessageView.as_view(), name='get_global_feed'),
]
