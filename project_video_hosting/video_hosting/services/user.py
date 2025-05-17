from typing import IO

from django.core.files.storage import default_storage

from video_hosting.serializers import LoadVideoSerializer
from video_hosting.models import User, Video
from video_hosting.exeptions import InvalidVideoId
from video_hosting.utils import VideoProcess


class VideoHostingService:
    def __init__(self):
        self.video_process = VideoProcess()

    def change_user(self, user_id: int, active: bool|None=True) -> None:
        user, created = User.objects.get_or_create(pk=user_id)

        if not created:
            user.is_active = active
            user.save()


    ###### ---->>>>>   РАБОТА С ВИДЕО   <<<<<---- ######
    def create_video(self, user: User, title: str, preview: IO, video: IO, duration: int) -> Video:
        user = User.objects.get(pk=21)   # временно    

        video = Video.objects.create(created_by=user, title=title, 
                                     preview=preview, video=video, duration=duration)

        return video

    def get_video(self, user_id: int, video_id: int) -> dict:
        try:
            video = Video.objects.get(created_by=user_id, pk=video_id, processed=True)

            serializer = LoadVideoSerializer(video)
            return serializer.data
        except Video.DoesNotExist:
            raise InvalidVideoId
        
    
    def process_video(self, input_file: str, resolutions: list, file_name: str, video_id: int):
        
        master = self.video_process.create_hls(input_file=input_file, resolutions=resolutions, file_name=file_name)

        video = Video.objects.get(pk=video_id)

        video.master_playlist = master
        video.video.delete()
        video.processed = True
        video.save()


    def delete_video(self, video_id: int, user_id: int):
        try:
            video = Video.objects.get(created_by=user_id, pk=video_id, processed=True)
        except Video.DoesNotExist:
            raise InvalidVideoId
        
        dir = video.master_playlist.name.split('/')[0]
        storage = default_storage
        storage.bucket.objects.filter(Prefix=dir).delete()
        video.delete()
    ###### ---->>>>>   РАБОТА С ВИДЕО   <<<<<---- ######

