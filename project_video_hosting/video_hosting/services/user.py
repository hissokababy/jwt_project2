from pydantic import BaseModel

from video_hosting.exeptions import InvalidUserStatus


def validate_message(message: dict) -> dict:
    class Message(BaseModel):
        id: int
        status: str
    try:
        body = Message(**message)
    except Exception as e:
        raise InvalidUserStatus(e)