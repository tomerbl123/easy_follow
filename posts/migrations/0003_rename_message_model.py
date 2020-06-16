from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_and_rename_fields'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Message',
        ),
    ]
