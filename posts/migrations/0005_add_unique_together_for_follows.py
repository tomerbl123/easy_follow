from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_refactor_follows_model'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mediauserfollow',
            unique_together={('following_user', 'followed_user')},
        ),
    ]
