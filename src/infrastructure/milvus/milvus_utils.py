from pymilvus import MilvusClient

from config import get_config

_milvus_connection = None


def create_milvus_connection():
    uri = get_config().milvus.uri
    token = get_config().milvus.token
    _milvus_connection = MilvusClient(uri=uri, token=token)
    if "papergeniedb" not in _milvus_connection.list_databases():
        _milvus_connection.create_database(db_name="papergeniedb")
    _milvus_connection.use_database(db_name="papergeniedb")


def get_milvus_connection() -> MilvusClient:
    return _milvus_connection
