from dataclasses import dataclass
from typing import Generic, TypeVar

from lrparser.utils.abstract_table_descriptor import TableDescriptor, RowDescriptor
from lrparser.utils.action_table_descriptor import ActionType, ActionColumnDescriptor, ActionRowDescriptor
from lrparser.utils.goto_table_descriptor import GotoRowDescriptor
from lrparser.utils.parser import Action, Finish, Reduce, Shift, State

R = TypeVar("R")
C = TypeVar("C")
V = TypeVar("V")


@dataclass
class Terminal:
    value: str

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value


class Table(Generic[R, C, V]):
    def __init__(self, descriptor: TableDescriptor):
        self.table: dict[R, dict[C, V]] = {}
        self._prepare(descriptor)

    def get(self, row: R, col: C) -> V:
        if row in self.table.keys():
            r = self.table[row]
            if col in r.keys():
                return r[col]
            raise KeyError(col, "->", row)
        raise KeyError(row, "<-", col)

    def _prepare(self, descriptor: TableDescriptor) -> None:
        for row in descriptor:
            self._inner_set(row)

    def _set(self, row: R, col: C, value: V) -> None:
        if row in self.table.keys():
            self.table.get(row).setdefault(col, value)
        else:
            self.table.setdefault(row, {col: value})

    def _inner_set(self, row: RowDescriptor) -> None:
        raise NotImplementedError()


class ActionTable(Table[State, Terminal, Action]):
    def __init__(self, descriptor: TableDescriptor):
        super().__init__(descriptor)

    def _inner_set(self, row: ActionRowDescriptor) -> None:
        r = State(row.state)
        for a in row.items:
            c = Terminal(a.from_state)
            v = self._get_action(a)
            self._set(r, c, v)

    def _get_action(self, action_descriptor: ActionColumnDescriptor) -> Action:
        if action_descriptor.type == ActionType.SHIFT:
            return Shift(
                State(action_descriptor.from_state),
                State(action_descriptor.to_state),
            )
        elif action_descriptor.type == ActionType.REDUCE:
            return Reduce(
                State(action_descriptor.from_state),
                State(action_descriptor.to_state),
                action_descriptor.count_args,
                action_descriptor.func,
            )
        elif action_descriptor.type == ActionType.FINISH:
            return Finish(
                State(action_descriptor.from_state),
                State(action_descriptor.to_state),
            )
        else:
            raise NotImplementedError()


class GotoTable(Table[State, State, str]):
    def __init__(self, descriptor: TableDescriptor):
        super().__init__(descriptor)

    def _inner_set(self, row: GotoRowDescriptor) -> None:
        r = State(row.state)
        for a in row.items:
            c = State(a.new_state)
            v = a.name_state
            self._set(r, c, v)
