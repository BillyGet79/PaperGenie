from abc import ABC, abstractmethod
from typing import Type, Optional

from pymilvus import CollectionSchema, Collection, connections, MilvusClient

from infrastructure.milvus.base_collection import BaseCollection


class BaseMilvusOperation(ABC):
    @property
    @abstractmethod
    def model_class(self) -> Type[BaseCollection]:
        pass

    @property
    @abstractmethod
    def metric_type(self) -> str:
        pass

    def __init__(self, milvus_client: MilvusClient):
        self.client = milvus_client
        self.add_collection()

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

    def delete_by_filters(self, filters: Optional[str] = None):
        client = self.client
        client.delete(collection_name=self.model_class.collection_name(), filter=filters)

    def get_by_ids(self, ids: list[int]) -> list[BaseCollection]:
        client = self.client
        raw_data = client.get(collection_name=self.model_class.collection_name(), ids=ids)
        return [self.model_class(**item) for item in raw_data]

    def get_by_filters(self, filters: Optional[str] = None) -> list[BaseCollection]:
        client = self.client
        raw_data = client.query(collection_name=self.model_class.collection_name(), filter=filters)
        return [self.model_class(**item) for item in raw_data]

    def distinct(self, field_name: str):
        client = self.client
        return client.query(collection_name=self.model_class.collection_name(), output_fields=[field_name])

    def ann_search(self, query_vector: list[float], top_k: int = 10, output_fields: Optional[list[str]] = None):
        client = self.client
        raw_data = client.search(
            collection_name=self.model_class.collection_name(),
            anns_field="vector",
            data=[query_vector],
            limit=top_k,
            search_params={
                "metric_type": self.metric_type,
            },
            output_fields=output_fields
        )
        return [self.model_class(**item) for item in raw_data[0]]
