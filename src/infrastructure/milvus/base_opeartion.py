from abc import ABC, abstractmethod
from typing import Type, Optional

from pymilvus import CollectionSchema, Collection, connections, MilvusClient

from infrastructure.milvus.base_collection import BaseCollection


class BaseMilvusOperation(ABC):
    @property
    @abstractmethod
    def model_class(self) -> Type[BaseCollection]:
        pass

    def __init__(self, milvus_client: MilvusClient):
        self.client = milvus_client

    def add_collection(self):
        client = self.client
        schema = client.create_schema(
            fields=self.model_class.fields(),
            description=self.model_class.collection_name()
        )
        if not client.has_collection(self.model_class.collection_name()):
            client.create_collection(collection_name=self.model_class.collection_name(), dimension=1024, schema=schema)

    def delete_collection(self):
        client = self.client
        if client.has_collection(self.model_class.collection_name()):
            client.drop_collection(self.model_class.collection_name())

    def insert(self, data: list[BaseCollection]):
        client = self.client
        raw_data: list[dict] = [item.__dict__ for item in data]
        client.insert(collection_name=self.model_class.collection_name(), data=raw_data)

    def delete_by_ids(self, ids: list[int]):
        client = self.client
        client.delete(collection_name=self.model_class.collection_name(), ids=ids)

    def delete_by_filters(self, filters: str):
        client = self.client
        client.delete(collection_name=self.model_class.collection_name(), filter=filters)

    def get_by_ids(self, ids: list[int]) -> list[BaseCollection]:
        client = self.client
        raw_data = client.get(collection_name=self.model_class.collection_name(), ids=ids)
        return [self.model_class(**item) for item in raw_data]

    def get_by_filters(self, filters: str) -> list[BaseCollection]:
        client = self.client
        raw_data = client.query(collection_name=self.model_class.collection_name(), filter=filters)
        return [self.model_class(**item) for item in raw_data]

    def distinct(self, field_name: str):
        client = self.client
        return client.query(collection_name=self.model_class.collection_name(), output_fields=[field_name])
