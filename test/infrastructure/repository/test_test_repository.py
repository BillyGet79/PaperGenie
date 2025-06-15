import sys

print(sys.path)

import pytest
from sqlmodel import Session

from infrastructure.model.test_model import TestModel
from infrastructure.repository.test_repository import TestRepository


@pytest.mark.usefixtures("session")
def test_test_repository_create(session: Session):
    repository = TestRepository(session)
    test_model = TestModel(name="Test Name", description="Test Description")
    repository.create(test_model)

    # Verify that the model was created
    created_model = repository.get_by_id(test_model.id)
    assert created_model is not None
    assert created_model.name == "Test Name"
    assert created_model.description == "Test Description"
