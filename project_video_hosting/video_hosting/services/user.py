from video_hosting.models import User
from video_hosting.exeptions import InvalidUserId, InvalidUserStatus


class VideoHostingService:
    def __init__(self, user: User=None):
        self.user = user

    def register_user(self, user_id: int):
        user, created = User.objects.get_or_create(pk=user_id)

        if not created:
            raise InvalidUserId(f'User with {user.pk} already exists!')


    def change_user_status(self, user_id: int, status: str):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise InvalidUserStatus(f'User with {user_id} does not exist!')

        user.status = status
        user.save()
        