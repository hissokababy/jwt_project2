# from project_video_hosting.celery import app

from video_hosting.services.user import VideoHostingService

from celery import shared_task
import time

@shared_task
def process_video_task() -> None:
    # service = VideoHostingService()
    # service.process_video()
    print('in task')
    time.sleep(20)
    print('task_done!')
