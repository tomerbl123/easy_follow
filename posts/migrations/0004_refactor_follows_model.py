from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_message_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaUserFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_follow', models.DateTimeField(auto_now_add=True)),
                ('followed_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='posts.MediaUser')),
                ('following_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='posts.MediaUser')),
            ],
        ),
        migrations.RenameField(
            model_name='message',
            old_name='date_created',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='creator_id',
            new_name='media_user',
        ),
        migrations.DeleteModel(
            name='MediaUsersFollow',
        ),
    ]
