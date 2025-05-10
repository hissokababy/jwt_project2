from typing import IO
from pathlib import Path

from django.core.files import File

from video_hosting.serializers import LoadVideoSerializer
from video_hosting.models import User, Video
from video_hosting.exeptions import InvalidVideoId


class VideoHostingService:
    def __init__(self):
        pass

    def change_user(self, user_id: int, active: bool|None=True) -> None:
        user, created = User.objects.get_or_create(pk=user_id)

        if not created:
            user.is_active = active
            user.save()


    ###### ---->>>>>   РАБОТА С ВИДЕО   <<<<<---- ######

    def create_video(self, user: User, title: str, preview: IO, video: IO, duration: int) -> None:
        user = User.objects.get(pk=21)   # временно    

        video = Video.objects.create(created_by=user, title=title, 
                                     preview=preview, video=video, duration=duration)


    def get_video(self, user_id: int, video_id: int) -> dict:
        try:
            video = Video.objects.get(created_by=user_id, pk=video_id)

            serializer = LoadVideoSerializer(video)
            return serializer.data
        except Video.DoesNotExist:
            raise InvalidVideoId
        
    
    def process_video(self):
        videos = Video.objects.filter(processed=False)

        if not videos.exists():
            pass
        
        ### создаем мастер плейлист ###
        video = Video.objects.get(pk=2)
        path = Path('project_video_hosting/master.m3u8')

        with path.open(mode='rb') as f:
            video.master_playlist = File(f, name='master.m3u8')
            video.save()
        ### создаем мастер плейлист ###

        
        


    ###### ---->>>>>   РАБОТА С ВИДЕО   <<<<<---- ######


