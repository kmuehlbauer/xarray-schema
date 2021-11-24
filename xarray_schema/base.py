import json
from abc import abstractmethod
from typing import Any, Dict, Hashable, Tuple, Union

DimsT = Tuple[Union[Hashable, None]]
ShapeT = Tuple[Union[int, None]]
ChunksT = Union[bool, Dict[Hashable, Union[int, None]]]


class SchemaError(Exception):
    '''Custom Schema Error'''

    pass


class BaseSchema:

    _json_schema: Dict[str, Any]

    @abstractmethod
    def validate(self, obj) -> None:
        pass

    @property
    @abstractmethod
    def json(self) -> Any:
        pass

    def to_json(self, **dumps_kws) -> str:
        return json.dumps(self.json, **dumps_kws)
