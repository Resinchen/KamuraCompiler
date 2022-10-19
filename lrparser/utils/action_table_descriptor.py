from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, NewType

from lrparser.utils.abstract_table_descriptor import (
    ColumnDescriptor,
    RowDescriptor,
    TableDescriptor,
)
from lrparser.utils.parser import Attribute, State


class ActionType(int, Enum):
    SHIFT = 0
    REDUCE = 1
    FINISH = 2


ReduceFunc = NewType(
    'ReduceFunc', Callable[[list[State]], dict[str, Attribute]]
)


@dataclass
class ActionColumnDescriptor(ColumnDescriptor):
    type: ActionType
    from_state: str
    to_state: str
    count_args: int | None = None
    func: Callable[[Any], Any] | None = None

    @classmethod
    def from_json(cls, data: dict):
        return cls(**data)


class ActionRowDescriptor(RowDescriptor):
    def __init__(self, state: str, items: list[ActionColumnDescriptor]):
        super().__init__(state, items)

    @classmethod
    def from_json(cls, data: dict):
        items = [
            ActionColumnDescriptor.from_json(item) for item in data['items']
        ]
        return cls(data['state'], items)


class ActionTableDescriptor(TableDescriptor):
    def __init__(self, rows: list[ActionRowDescriptor]):
        super().__init__(rows)

    @classmethod
    def from_json(cls, data: list):
        items = [ActionRowDescriptor.from_json(item) for item in data]
        return cls(items)
