# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, max_length=70, blank=False, verbose_name=_('Email'))
    email_confirmed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name=_('Birthdate'),)
    telephone = models.CharField(max_length=50, blank=True, verbose_name=_('Phone'),)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email',]


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Token(Token):
    """create multiple tokens per user - override default rest_framework Token class
    replace model one-to-one relationship with foreign key"""

    key = models.CharField(max_length=40, db_index=True, unique=True)
    user = models.ForeignKey(User, related_name='auth_token', on_delete=models.CASCADE)
