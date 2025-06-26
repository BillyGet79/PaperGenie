from typing import Type

from infrastructure.db.base_model import T
from infrastructure.db.base_repository import CommonRepository
from infrastructure.db.database import get_session
from infrastructure.model.init_model import InitModel


class InitRepository(CommonRepository):
    @property
    def model_class(self) -> Type[T]:
        return InitModel
