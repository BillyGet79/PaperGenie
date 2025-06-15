from typing import Type

from infrastructure.database.base_model import T
from infrastructure.database.base_repository import CommonRepository
from infrastructure.database.database import get_session
from infrastructure.model.test_model import TestModel


class TestRepository(CommonRepository):
    @property
    def model_class(self) -> Type[T]:
        return TestModel


if __name__ == '__main__':
    with get_session() as session:
        repository = TestRepository(session)
        test_model = TestModel(name="Test Name", description="Test Description")
        repository.create(test_model)

        # Verify that the model was created
        created_model = repository.get_by_id(test_model.id)
        print(created_model)

