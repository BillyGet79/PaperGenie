from infrastructure.db.database import get_session, create_session
from infrastructure.model.test_model import TestModel
from infrastructure.repository.test_repository import TestRepository
from infrastructure.utils.log_utils import logger


class TestTestRepository:

    @classmethod
    def setUpClass(cls):
        cls.session = create_session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def test_get_by_id(self):
        repository = TestRepository(self.session)
        test_model = TestModel(name="Test Name", description="Test Description")
        repository.create(test_model)
        logger.info(f"Creating test model: {test_model}")

        # Verify that the model was created
        created_model = repository.get_by_id(test_model.id)
        print(created_model)
