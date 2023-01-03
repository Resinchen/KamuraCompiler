import abc
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from lrparser.utils.parser import (
    Action,
    ActionType,
    Finish,
    Reduce,
    Shift,
    State,
)

R = TypeVar('R')
C = TypeVar('C')
V = TypeVar('V')


@dataclass
class Terminal:
    value: str

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Terminal):
            return False
        return self.value == other.value


class Table(abc.ABC, Generic[R, C, V]):
    def __init__(self, descriptor: dict[str, dict[str, Any]]):
        self.table: dict[R, dict[C, V]] = {}
        self.__name__ = 'Abstract Table'
        self._prepare(descriptor)

    def get(self, row: R, col: C) -> V:
        if row in self.table.keys():
            r = self.table[row]
            if col in r.keys():
                return r[col]
            raise KeyError(f'{row} -> {col} {self.__name__}')
        raise KeyError(f'{row} <- {col} {self.__name__}')

    def _prepare(self, descriptor: dict[str, dict[str, Any]]) -> None:
        for row in descriptor.items():
            self._inner_set(row)

    def _set(self, row: R, col: C, value: V) -> None:
        if row in self.table.keys():
            self.table[row].setdefault(col, value)
        else:
            self.table.setdefault(row, {col: value})

    @abc.abstractmethod
    def _inner_set(self, row: tuple[str, dict[str, Any]]) -> None:
        pass


class ActionTable(Table[State, Terminal, Action]):
    def __init__(self, descriptor: dict[str, dict[str, Any]]):
        super().__init__(descriptor)
        self.__name__ = 'ActionTable'

    def _inner_set(self, row: tuple[str, dict[str, Any]]) -> None:
        r = State(row[0])
        for a in row[1].items():
            if a[1] is None:
                continue
            c = Terminal(a[0])
            v = self._get_action(a[1])
            self._set(r, c, v)

    def _get_action(self, action_cell_descriptor: Any) -> Action:
        match action_cell_descriptor.type:  # noqa: R503
            case ActionType.SHIFT:
                return Shift(
                    State(action_cell_descriptor.from_state),
                    State(action_cell_descriptor.to_state),
                )
            case ActionType.REDUCE:
                return Reduce(
                    State(action_cell_descriptor.from_state),
                    State(action_cell_descriptor.to_state),
                    action_cell_descriptor.count_args,
                    action_cell_descriptor.func,
                )
            case ActionType.FINISH:
                return Finish(
                    State(action_cell_descriptor.from_state),
                    State(action_cell_descriptor.to_state),
                )
            case _:
                raise NotImplementedError()


class GotoTable(Table[State, State, str]):
    def __init__(self, descriptor: dict[str, dict[str, Any]]):
        super().__init__(descriptor)
        self.__name__ = 'GotoTable'

    def _inner_set(self, row: tuple[str, dict[str, Any]]) -> None:
        r = State(row[0])
        for a in row[1].items():
            if a[1] is None:
                continue
            c = State(a[0])
            v = a[1].name_state
            self._set(r, c, v)
