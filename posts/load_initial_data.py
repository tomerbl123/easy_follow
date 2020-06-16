import os
import django
django.setup()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easy_follow.settings')

from posts import models


def load_initial_users():
    models.MediaUser.objects.bulk_create([
        models.MediaUser(username='user1'),
        models.MediaUser(username='user2'),
        models.MediaUser(username='user3'),
        models.MediaUser(username='user4'),
        models.MediaUser(username='user5'),
    ])


# def load_initial_messages(user1, user2, user3, user4, user5):
#     models.MediaUser.objects.bulk_create([
#         models.Message(content='User1 Message - first', media_user=user1),
#         models.Message(content='User1 Message - second', media_user=user1),
#         models.Message(content='User2 Message', media_user=user2),
#         models.Message(content='User3 Message', media_user=user3),
#         models.Message(content='User4 Message', media_user=user4),
#         models.Message(content='User5 Message', media_user=user5),
#     ])
#
#
# def load_initial_follows(user1, user2, user3, user4, user5):
#     models.MediaUser.objects.bulk_create([
#         models.MediaUserFollow(following_user=1, followed_user=user2),
#         models.MediaUserFollow(following_user=1, followed_user=user3),
#         models.MediaUserFollow(following_user=2, followed_user=user4),
#         models.MediaUserFollow(following_user=3, followed_user=user5),
#         models.MediaUserFollow(following_user=4, followed_user=user1),
#     ])


if __name__ == '__main__':
    load_initial_users()
    user1 = models.MediaUser.objects.get(username='user1')
    user2 = models.MediaUser.objects.get(username='user2')
    user3 = models.MediaUser.objects.get(username='user3')
    user4 = models.MediaUser.objects.get(username='user4')
    user5 = models.MediaUser.objects.get(username='user5')

    # load_initial_messages(user1, user2, user3, user4, user5)
    # load_initial_follows(user1, user2, user3, user4, user5)
