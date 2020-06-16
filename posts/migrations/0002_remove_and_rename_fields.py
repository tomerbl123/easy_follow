from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mediauser',
            old_name='nickname',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='mediauser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='mediauser',
            name='last_name',
        ),
    ]
