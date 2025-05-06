from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        abstract = True
        
class UserStatus(models.TextChoices):
    ACTIVE = 'AC', ""
    INACTIVE = 'IN', ""
    BLOCKED = 'BL', ""

class User(CommonInfo):
    ACTIVE = 'AC'
    INACTIVE = 'IN'
    BLOCKED = 'BL'

    STATUS_CHOICES = {
        ACTIVE: 'Active',
        INACTIVE: 'Inactive',
        BLOCKED: 'Blocked'
    }
    
    id = models.PositiveIntegerField(verbose_name='Ид пользователя', primary_key=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)

    def __str__(self):
        return f'Пользователь {self.id}'
    
    class Meta:
        verbose_name = 'Пользователя хостинга'
        verbose_name_plural = 'Пользователи хостинга'


class Video(CommonInfo):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos', 
                                   verbose_name='Автор видео')
    title = models.CharField(max_length=255, verbose_name='Название видео')
    preview = models.ImageField(upload_to='video/previews', verbose_name='Обложка видео')
    video = models.FileField(upload_to='videos/', verbose_name='Видео')
    duration = models.DurationField(verbose_name='Длительность видео')


    def __str__(self):
        return f'Видео {self.pk}, Автор {self.created_by}'
    
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
    

class WatchedVideo(CommonInfo):
    viewer = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Зритель', blank=True, null=True)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name='Видео')
    watching_at = models.PositiveIntegerField(verbose_name='Точка просмотра видео', null=True)

    def __str__(self):
        return f'Видео {self.video_id}, Зритель {self.viewer}'
    
    class Meta:
        verbose_name = 'Просмотренное Видео'
        verbose_name_plural = 'Просмотренное Видео'