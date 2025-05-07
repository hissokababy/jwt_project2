from video_hosting.models import User
from video_hosting.exeptions import InvalidUserId


class VideoHostingService:
    def __init__(self):
        pass

    def change_user(self, user_id: int, active: bool|None=True):
        user, created = User.objects.get_or_create(pk=user_id)

        if not created:
            user.is_active = active
            user.save()
        