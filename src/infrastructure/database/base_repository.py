import abc
from abc import abstractmethod
from typing import Any, Generic, Type, List, Optional

from sqlmodel import Session, select, func, delete

from infrastructure.database.base_model import T
from infrastructure.database.page import PageData
from infrastructure.error.bad_request_error import BadRequestError


class AbstractRepository(abc.ABC):

    @abstractmethod
    def create(self, model: T):
        pass

    @abstractmethod
    def delete_by_id(self, id: int):
        pass

    @abstractmethod
    def update(self, model: T):
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def page(self, page_size: int, page_num: int, filters: Optional[dict[str, Any]] = None):
        pass


class CommonRepository(AbstractRepository, Generic[T]):

    def __init__(self, session: Session):
        self._session = session

    @property
    @abstractmethod
    def model_class(self) -> Type[T]:
        pass

    def delete_by_id(self, id: int) -> bool:
        obj = self.get_by_id(id)
        if obj is None:
            return False
        session = self._session
        session.delete(obj)
        session.commit()
        return True

    def remove(self, filters: dict = None):
        statement = delete(self.model_class)
        if filters:
            statement = self.__apply_filters(statement, filters)
        self._session.exec(statement)
        self._session.commit()

    def update(self, model: T):
        session = self._session
        db_model: Optional[T] = session.get(self.model_class, model.id)
        if db_model is None:
            raise ValueError(f"not found {model.id} in db")
        db_model.sqlmodel_update(model.__dict__)
        session.add(db_model)
        session.commit()
        session.refresh(db_model)
        return db_model

    def get_by_id(self, id: int):
        return self._session.get(self.model_class, id)

    def exist_by_id(self, id: int):
        return self.get_by_id(id) is not None

    def exist(self, filters: dict):
        return self.count(filters=filters) > 0

    def list(self, filters: Optional[dict[str, Any]] = None, order_by=None) -> list[T]:
        statement = select(self.model_class)
        if filters:
            statement = self.__apply_filters(statement, filters)
        if order_by:
            statement = statement.order_by(*order_by)
        return [x for x in self._session.exec(statement).all()]

    def page(self, page_size: int = 10, page_num: int = 1, filters: Optional[dict[str, Any]] = None, order_by=None) -> \
    PageData[T]:
        total = self.count(filters)
        if page_num < 1:
            page_num = 1
        statement = select(self.model_class)
        if filters:
            statement = self.__apply_filters(statement, filters)
        if order_by:
            statement = statement.order_by(*order_by)
        offset = (page_num - 1) * page_size
        statement = statement.offset(offset).limit(page_size)
        items = [x for x in self._session.exec(statement).all()]

        return PageData(
            items=items,
            total=total,
            page_size=page_size,
            page_num=page_num
        )

    def create(self, model: T):
        session = self._session
        session.add(model)
        session.commit()
        session.refresh(model)
        return model

    def create_batch(self, models: List[T]):
        session = self._session
        session.bulk_save_objects(models)
        session.commit()

    def __apply_filters(self, statement, filters):
        """
        filters字段处理，通过字段处理实现in和like判断条件操作
        之后有需求可以接着在operator判断条件后面继续添加
        字段如果有操作，请在字段key后面添加"__"+operator
        示例： filters = {"name__like": "张三"}
        :param statement:
        :param filters:
        :return:
        """
        for field_str, value in filters.items():
            if not value:
                continue
            if "__" in field_str:
                field_info = field_str.split("__")
                field, operator = field_info[0], field_info[1]
            else:
                field, operator = field_str, None
            model_field = getattr(statement, field)
            if model_field is None:
                raise BadRequestError(f"not found {field} in class: {self.model_class.__name__}")
            if not operator:
                statement = statement.where(getattr(self.model_class, field) == value)
            elif "in" == operator:
                statement = statement.where(getattr(self.model_class, field).in_(value))
            elif "like" == operator:
                statement = statement.where(getattr(self.model_class, field).like(f"%{value}%"))
            else:
                raise BadRequestError(f"not support {field_str}")
        return statement

    def count(self, filters: Optional[dict[str, Any]] = None):
        statement = select(func.count()).select_from(self.model_class)
        if filters:
            statement = self.__apply_filters(statement, filters)
        return self._session.exec(statement).one()
