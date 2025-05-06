from video_hosting.models import User
from video_hosting.exeptions import InvalidUserId, InvalidUserActivity


class VideoHostingService:
    def __init__(self, user: User=None):
        self.user = user

    def register_user(self, user_id: int):
        user, created = User.objects.get_or_create(pk=user_id)

        if not created:
            raise InvalidUserId(f'User with {user.pk} already exists!')


    def change_user_activity(self, user_id: int, active: bool):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise InvalidUserActivity(f'User with {user_id} does not exist!')

        user.is_active = active
        user.save()
        