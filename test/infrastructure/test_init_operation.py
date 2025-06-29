import unittest

from infrastructure.milvus.collection_impl.init_collection import InitCollection
from infrastructure.milvus.milvus_utils import MilvusUtils
from infrastructure.milvus.operation_impl.init_operation import InitOperation


class TestInitOperation(unittest.TestCase):

    def test_init_operation(self):
        init_operation = InitOperation(MilvusUtils.get_milvus_connection())
        init_operation.delete_collection()
        init_operation.add_collection()
        init_model = InitCollection(
            vector=[0.0, 0.2, 0.4, .06, 0.8],
            description="test_model"
        )
        init_operation.insert([init_model])
        print(init_operation.get_by_filters())
