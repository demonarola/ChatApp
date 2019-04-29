# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, max_length=70, blank=False, verbose_name=_('Email'))
    email_confirmed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name=_('Birthdate'),)
    telephone = models.CharField(max_length=50, blank=True, verbose_name=_('Phone'),)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email',]
