from pydantic import BaseModel

from jwtapp.exeptions import InvalidUserActivity

class UserMessage(BaseModel):
    id: int
    active: bool|None =True


class MessageValidators:
    def __init__(self):
        pass

    def validate_user_activity(self, id: int, active: bool) -> str:
        try:
            body = UserMessage(id=id, active=active).model_dump_json()
            return body
        except Exception as e:
            raise InvalidUserActivity(e)

    def validate_user_id(self, id: int) -> str:
        try:
            body = UserMessage(id=id).model_dump_json()
            return body
        except Exception as e:
            raise InvalidUserActivity(e)
        
    