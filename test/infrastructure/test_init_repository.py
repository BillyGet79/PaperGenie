from infrastructure.db.database import get_session, create_session
from infrastructure.model.init_model import InitModel
from infrastructure.repository.init_repository import InitRepository
from infrastructure.utils.log_utils import logger
import unittest


class TestInitRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = create_session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def test_get_by_id(self):
        repository = InitRepository(TestInitRepository.session)  # 使用类级别的 session
        test_model = InitModel(name="Test Name", description="Test Description")
        repository.create(test_model)
        logger.info(f"Creating test model: {test_model}")

        # Verify that the model was created
        created_model = repository.get_by_id(test_model.id)
        print(created_model)
