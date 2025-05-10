from project_video_hosting.celery import app

from video_hosting.services.user import VideoHostingService


@app.task
def check() -> None:
    service = VideoHostingService()
    # service.check_task_date()

