from dataclasses import dataclass


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
