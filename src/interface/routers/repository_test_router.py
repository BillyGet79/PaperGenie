from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import Session

from infrastructure.db.database import get_session
from infrastructure.model.test_model import TestModel
from infrastructure.repository.test_repository import TestRepository
from infrastructure.utils.log_utils import logger
from interface.schemas.base_response import BaseResponse

router = APIRouter(prefix="/repository")

@router.get("/test", summary="Repository Test Endpoint")
def repository_test(session: Session = Depends(get_session)):
    repository = TestRepository(session)
    test_model = TestModel(name="Test Name", description="Test Description")
    repository.create(test_model)
    logger.info(f"Creating test model: {test_model}")

    # Verify that the model was created
    created_model = repository.get_by_id(test_model.id)
    return BaseResponse.success(created_model)