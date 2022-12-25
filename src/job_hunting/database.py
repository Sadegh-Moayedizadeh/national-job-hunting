from contextlib import contextmanager
from typing import Union, Generator, Dict, Any, List
from pathlib import Path
import json


class Query:
    def __init__(self, database_path: Union[str, Path]) -> None:
        self._database_path = database_path \
            if isinstance(database_path, Path) else Path(database_path)

    def get(self, table_name: str, id: str) -> None:
        with self._get_session(table_name) as table:
            result = list(filter(lambda d: d['id'] == id, table))
        if len(result) == 0:
            raise ValueError('There is no entry with the given id.')
        if len(result) > 1:
            raise ValueError('There is more than one entry with the given id.')
        return result.pop()

    def update(self, **kwargs) -> None:
        pass

    @contextmanager
    def _get_session(
        self, table_name: str
    ) -> Generator[List[Dict[str, Any]], None, None]:
        table_path = self._database_path / (table_name + '.json')
        json_file = open(table_path, 'r')
        json_obj = json.load(json_file)
        yield json_obj
        json_file.close()

    @contextmanager
    def _update_session(
        self, table_name: str
    ) -> Generator[List[Dict[str, Any]], None, None]:
        table_path = self._database_path / (table_name + '.json')
        json_file = open(table_path, 'r+')
        json_obj = json.load(json_file)
        yield json_obj
        json_file.seek(0)
        json.dump(json_obj, json_file)
        json_file.truncate()
        json_file.close()
