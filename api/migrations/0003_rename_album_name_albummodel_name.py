# Generated by Django 4.2.5 on 2023-09-08 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_personmodel_rename_album_albummodel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albummodel',
            old_name='album_name',
            new_name='name',
        ),
    ]