from interface.schemas.base_response import CodeEnum


class CustomException(Exception):
    def __init__(self, **kwargs):
        self.__code: CodeEnum = kwargs.get("code")
        self.__message: str = kwargs.get("message")

    @property
    def code(self):
        return self.__code

    @property
    def message(self):
        return self.__message