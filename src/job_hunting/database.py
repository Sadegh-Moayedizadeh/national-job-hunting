from contextlib import contextmanager
from typing import Union, Generator, IO
from pathlib import Path
import json


class Query:
    def __init__(self, database_path: Union[str, Path]) -> None:
        self._database_path = database_path \
            if isinstance(database_path, Path) else Path(database_path)

    @contextmanager
    def _update_session(self, table_name: str) -> Generator[IO, None, None]:
        table_path = self._database_path / table_name
        json_file = open(table_path)
        json_obj = json.load(json_file)
        yield json_obj
        new_json_obj = yield
        json_file.seek(0)
        json.dump(new_json_obj, json_file)
        json_file.truncate()
        json_file.close()
