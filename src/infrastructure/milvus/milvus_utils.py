from pymilvus import MilvusClient

from config import get_config


class MilvusUtils:
    _milvus_connection = None

    @classmethod
    def get_milvus_connection(cls):
        uri = get_config().milvus.uri
        token = get_config().milvus.token
        cls._milvus_connection = MilvusClient(uri=uri, token=token)
        if "papergeniedb" not in cls._milvus_connection.list_databases():
            cls._milvus_connection.create_database(db_name="papergeniedb")
        cls._milvus_connection.use_database(db_name="papergeniedb")
        return cls._milvus_connection
