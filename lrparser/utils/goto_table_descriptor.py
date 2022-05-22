from dataclasses import dataclass

from lrparser.utils.abstract_table_descriptor import (
    ColumnDescriptor,
    RowDescriptor,
    TableDescriptor,
)


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
