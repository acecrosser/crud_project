from __future__ import unicode_literals
from django.contrib.auth.base_user import BaseUserManager
from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):

    def _create_user(self, username, password, **plus_fields):
        if not username:
            raise ValueError('Введите имя')
        try:
            with transaction.atomic():
                user = self.model(username=username, **plus_fields)
                hash_password = make_password(password)
                print(hash_password)
                user.set_password(hash_password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, username, password, **plus_fields):
        plus_fields.setdefault('is_staff', True)
        plus_fields.setdefault('is_superuser', True)
        return self._create_user(username, password=password, **plus_fields)

    def create_superuser(self, username, password, **plus_fields):
        plus_fields.setdefault('is_staff', True)
        plus_fields.setdefault('is_superuser', True)
        return self._create_user(username, password=password, **plus_fields)


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

