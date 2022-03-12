from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, NewType, Optional

from lrparser.utils.parser import Attribute, State


class ActionType(int, Enum):
    SHIFT = 0
    REDUCE = 1
    FINISH = 2


ReduceFunc = NewType("ReduceFunc", Callable[[list[State]], dict[str, Attribute]])

# Abstract table


@dataclass
class ColumnDescriptor:
    pass


@dataclass
class RowDescriptor:
    state: str
    items: list[ColumnDescriptor]


class TableDescriptor:
    def __init__(self, rows: list[RowDescriptor]):
        self.rows = rows

    def __getitem__(self, item):
        return self.rows[item]

    def __str__(self):
        return f"{self.__class__.__name__}(rows={self.rows})"


# Goto Table


@dataclass
class GotoColumnDescriptor(ColumnDescriptor):
    new_state: str
    name_state: str

    @classmethod
    def from_json(cls, data: dict):
        return cls(**data)


class GotoRowDescriptor(RowDescriptor):
    def __init__(self, state: str, items: list[GotoColumnDescriptor]):
        super().__init__(state, items)

    @classmethod
    def from_json(cls, data: dict):
        items = [GotoColumnDescriptor.from_json(item) for item in data["items"]]
        return cls(data["state"], items)


class GotoTableDescriptor(TableDescriptor):
    def __init__(self, rows: list[GotoRowDescriptor]):
        super().__init__(rows)

    @classmethod
    def from_json(cls, data: dict):
        items = [GotoRowDescriptor.from_json(item) for item in data]
        return cls(items)


# Action Table


@dataclass
class ActionColumnDescriptor(ColumnDescriptor):
    type: ActionType
    from_state: str
    to_state: str
    count_args: Optional[int] = None
    func: Optional[Callable[[Any], Any]] = None

    @classmethod
    def from_json(cls, data: dict):
        return cls(**data)


class ActionRowDescriptor(RowDescriptor):
    def __init__(self, state: str, items: list[ActionColumnDescriptor]):
        super().__init__(state, items)

    @classmethod
    def from_json(cls, data: dict):
        items = [ActionColumnDescriptor.from_json(item) for item in data["items"]]
        return cls(data["state"], items)


class ActionTableDescriptor(TableDescriptor):
    def __init__(self, rows: list[ActionRowDescriptor]):
        super().__init__(rows)

    @classmethod
    def from_json(cls, data: dict):
        items = [ActionRowDescriptor.from_json(item) for item in data]
        return cls(items)
