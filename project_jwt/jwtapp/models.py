from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ACTIVE = 'AC'
    INACTIVE = 'IN'
    BLOCKED = 'BL'

    STATUS_CHOICES = {
        ACTIVE: 'Active',
        INACTIVE: 'Inactive',
        BLOCKED: 'Blocked'
    }

    send_code = models.IntegerField(verbose_name='Код подтверждения', blank=True, null=True)
    time_send = models.DateTimeField(verbose_name='Дата отправки кода', blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='Active', max_length=50)

    def __str__(self):
        return f'Пользователь {self.pk} {self.status}'

class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', blank=True, null=True)

    class Meta:
        abstract = True


class Session(CommonInfo):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions', verbose_name='Пользователь')
    user_ip = models.GenericIPAddressField(max_length=155, verbose_name='Ip устройства пользователя', blank=True, null=True, unique=True)
    refresh_token = models.TextField(verbose_name='Refresh token', blank=True, null=True)
    device_type = models.CharField(max_length=150, verbose_name='Тип устройства', blank=True, null=True, default='mobile')
    active = models.BooleanField(default=False, verbose_name='Активная сессия')

    def __str__(self):
        return f'(id: {self.pk}) Сессия пользователя: {self.user.username} | {self.active}'

    class Meta:
        verbose_name = 'Сессия'
        verbose_name_plural = 'Сессии'

