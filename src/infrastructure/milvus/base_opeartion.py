from abc import ABC
from typing import Type

from pymilvus import CollectionSchema, Collection, connections

from infrastructure.milvus.base_collection import BaseCollection
from infrastructure.milvus.milvus_utils import MilvusUtils


class BaseMilvusOperation(ABC):
    def __init__(self, model_class: Type[BaseCollection]):
        self.model_class = model_class

    def get_connection(self) -> Collection:
        return MilvusUtils.get_milvus_connection()

    def add_collection(self):
        schema = CollectionSchema(
            fields=self.model_class.fields(),
            description=self.model_class.collection_name()
        )
        conn = self.get_connection()
        if not conn.has_collection(self.model_class.collection_name()):
            conn.create_collection(name=self.model_class.collection_name(), schema=schema)

    def delete_collection(self):
        conn = self.get_connection()
        if conn.has_collection(self.model_class.collection_name()):
            conn.drop_collection(self.model_class.collection_name())

    def insert(self, data: list[BaseCollection]):
        collection = Collection(name=self.model_class.collection_name())
        raw_data = [item.dict for item in data]
        collection.insert(raw_data)
