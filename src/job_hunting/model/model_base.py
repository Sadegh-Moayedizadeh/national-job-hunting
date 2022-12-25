from __future__ import annotations
from job_hunting.database import Query
from typing import Type


def create_base(database_path) -> Type[ModelBase]:
    ModelBase.query = Query(database_path)
    return ModelBase


class ModelBase:
    table_name: str = None
    query: Query

    def update(self) -> None:
        pass

    def create(self) -> None:
        pass

    def delete(self) -> None:
        pass

    @classmethod
    def get(cls, id: str) -> None:
        return cls.query.get(table_name=cls.table_name, id=id)


## client
# user = User(...)
# user.save()

# user = User.get(id='')
