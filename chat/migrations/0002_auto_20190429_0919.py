# Generated by Django 2.0 on 2019-04-29 09:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='seller',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
