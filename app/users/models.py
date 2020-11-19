from __future__ import unicode_literals
from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **plus_fields):
        if not email:
            raise ValueError('Электронная почта должна быть указана')
        try:
            with transaction.atomic():
                user = self.model(email=email, **plus_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, email, password=None, **plus_fields):
        plus_fields.setdefault('is_staff', False)
        plus_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **plus_fields)

    def create_superuser(self, email, password, **plus_fields):
        plus_fields.setdefault('is_staff', True)
        plus_fields.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **plus_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=140, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

