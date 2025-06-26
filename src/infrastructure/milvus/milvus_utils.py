from pymilvus import connections, Collection

from config import get_config


class MilvusUtils:
    _milvus_connection = None

    @classmethod
    def get_milvus_connection(cls) -> Collection:
        if cls._milvus_connection is None:
            host = get_config().milvus.host
            port = get_config().milvus.port
            _milvus_connection = connections.connect(host=host, port=port)
        return _milvus_connection
