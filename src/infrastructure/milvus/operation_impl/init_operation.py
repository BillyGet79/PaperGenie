from typing import Type

from infrastructure.milvus.base_collection import BaseCollection
from infrastructure.milvus.base_operation import BaseMilvusOperation
from infrastructure.milvus.collection_impl.init_collection import InitCollection


class InitOperation(BaseMilvusOperation):
    @property
    def model_class(self) -> Type[BaseCollection]:
        return InitCollection


    @property
    def metric_type(self) -> str:
        return "COSINE"