from rest_framework.exceptions import APIException
from rest_framework import status

class InvalidUserId(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = ('invalid id')
    default_code = 'invalid_user_id'