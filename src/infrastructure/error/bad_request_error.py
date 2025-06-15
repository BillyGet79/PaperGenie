from infrastructure.error.custom_error import CustomException
from interface.schemas.base_response import CodeEnum


class BadRequestError(CustomException):
    def __init__(self, message):
        super().__init__(code=CodeEnum.BAD_REQUEST, message=f"bad request: {message}")