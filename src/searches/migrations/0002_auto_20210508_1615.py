# Generated by Django 2.2 on 2021-05-08 16:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('searches', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QearchQuery',
            new_name='SearchQuery',
        ),
    ]
