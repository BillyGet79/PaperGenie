from abc import ABC, abstractmethod

from pydantic.v1 import BaseModel
from pymilvus import FieldSchema, CollectionSchema, Collection

from config import get_config
from infrastructure.milvus.milvus_utils import MilvusUtils


class BaseCollection(ABC, BaseModel):
    id: int

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
