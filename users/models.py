from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class User(AbstractUser):
    phone = models.CharField(unique=True, verbose_name='номер телефона')
    username = None
    password = None
    otp = models.CharField(max_length=6, verbose_name='одноразовый код', null=True, blank=True)
    invite_code = models.CharField(unique=True, max_length=6, verbose_name='инвайт код')
    invited_users = models.ManyToManyField('User', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
