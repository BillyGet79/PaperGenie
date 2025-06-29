from abc import ABC, abstractmethod
from typing import Optional

from pydantic.v1 import BaseModel
from pymilvus import FieldSchema


class BaseCollection(ABC, BaseModel):
    id: Optional[int] = None
    vector: list[float]

    @classmethod
    @abstractmethod
    def fields(cls) -> list[FieldSchema]:
        """
        子类必须定义字段 schema
        :return:
        """
        pass

    @classmethod
    @abstractmethod
    def collection_name(cls) -> str:
        """
        子类必须定义 collection_name
        :return:
        """
        pass
