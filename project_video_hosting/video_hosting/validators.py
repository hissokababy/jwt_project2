from pydantic import BaseModel

from video_hosting.exeptions import InvalidUserActivity


class UserActivity(BaseModel):
    id: int
    active: bool


class UserId(BaseModel):
    id: int


class ValidateMessage:
    
    @classmethod
    def validate_activity(cls, body: str) -> UserActivity:
        try:
            message = UserActivity.model_validate_json(body)
            return message
        except Exception as e:
            raise InvalidUserActivity(e)
        
    @classmethod
    def validate_user_id(cls, body: str) -> UserId:
        try:
            message = UserId.model_validate_json(body)
            return message
        except Exception as e:
            raise InvalidUserActivity(e)
