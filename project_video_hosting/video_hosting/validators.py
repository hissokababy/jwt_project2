from pydantic import BaseModel

from video_hosting.exeptions import InvalidUserStatus


class Status(BaseModel):
    id: int
    status: str


class UserId(BaseModel):
    id: int


class ValidateMessage:
    
    @classmethod
    def validate_status(cls, body: str) -> Status:
        try:
            message = Status.model_validate_json(body)
            return message
        except Exception as e:
            raise InvalidUserStatus(e)
        
    @classmethod
    def validate_user_id(cls, body: str) -> Status:
        try:
            message = UserId.model_validate_json(body)
            return message
        except Exception as e:
            raise InvalidUserStatus(e)
