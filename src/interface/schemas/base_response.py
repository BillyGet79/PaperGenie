import enum
from typing import Optional, Any

from pydantic import BaseModel


class CodeEnum(enum.Enum):
    SUCCESS = "200"
    BAD_REQUEST = "400"
    INTERNAL_ERROR = "500"

class BaseResponse(BaseModel):
    code: str
    message: str
    data: Optional[Any] = None

    @staticmethod
    def success(data: Optional[Any] = None):
        return BaseResponse(code=CodeEnum.SUCCESS.value, message="success", data=data)

    @staticmethod
    def error(code: CodeEnum, message: str, data: Optional[Any] = None):
        return BaseResponse(code=code.value, message=message, data=data)

    @staticmethod
    def internal_error():
        return BaseResponse(code=CodeEnum.INTERNAL_ERROR.value, message="internal error", data=None)