from pymilvus import FieldSchema, DataType

from infrastructure.milvus.base_collection import BaseCollection


class InitCollection(BaseCollection):
    description: str
    @classmethod
    def fields(cls) -> list[FieldSchema]:
        return [
            FieldSchema(name="description", dtype=DataType.VARCHAR, max_length=256),
        ]


    @classmethod
    def collection_name(cls) -> str:
        return "InitCollection"