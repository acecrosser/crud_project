from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_create = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

