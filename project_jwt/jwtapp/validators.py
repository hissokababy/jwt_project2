from pydantic import BaseModel

from jwtapp.exeptions import InvalidUserStatus


class MessageValidators:
    def __init__(self):
        pass

    def validate_user_status(self, id: int, status: str) -> str:
        class Status(BaseModel):
            id: int
            status: str
        try:
            body = Status(id=id, status=status).model_dump_json()
            return body
        except Exception as e:
            raise InvalidUserStatus(e)

    def validate_user_id(self, id: int) -> str:
        class UserId(BaseModel):
            id: int
        try:
            body = UserId(id=id).model_dump_json()
            return body
        except Exception as e:
            raise InvalidUserStatus(e)
        
    