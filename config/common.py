import re
from typing import Any, Callable

from lrparser.utils.parser import ActionType


class TokenDesctiptor:
    def __init__(self, name: str, pattern: str):
        self.name = name
        self.pattern = re.compile(pattern)

    def __repr__(self) -> str:
        return f'Token({self.name}, r"{self.pattern.pattern}")'


class ActionCellDescriptor:
    def __init__(
        self,
        type: ActionType,
        from_state: str,
        to_state: str,
        count_args: int | None = None,
        func: Callable[..., Any] | None = None,
    ):
        self.type = type
        self.from_state = from_state
        self.to_state = to_state
        self.count_args = count_args
        self.func = func

    def __repr__(self) -> str:
        match self.type:
            case ActionType.SHIFT:
                return f'Shift({self.from_state}->{self.to_state})'
            case ActionType.REDUCE:
                return f'Reduce({self.from_state}->{self.to_state}, {self.func.__name__})'
            case ActionType.FINISH:
                return f'Finish({self.from_state}->{self.to_state})'
            case _:
                raise AttributeError('Undefined type')


class GotoCellDescriptor:
    def __init__(self, new_state: str, name_state: str):
        self.new_state = new_state
        self.name_state = name_state

    def __repr__(self) -> str:
        return f'GoTo({self.new_state}=>{self.name_state})'


class Config:
    def __init__(self, tokens, action_table, goto_table):
        self.tokens = tokens
        self.action_table = action_table
        self.goto_table = goto_table


def make_shift_action(from_state: str, to_state: str) -> ActionCellDescriptor:
    return ActionCellDescriptor(type=ActionType.SHIFT, from_state=from_state, to_state=to_state)


def make_finish_action(from_state: str) -> ActionCellDescriptor:
    return ActionCellDescriptor(type=ActionType.FINISH, from_state=from_state, to_state='ok')


def make_reduce_action(from_state: str, to_state: str, func: Callable[..., Any]) -> ActionCellDescriptor:
    return ActionCellDescriptor(
        type=ActionType.REDUCE,
        from_state=from_state,
        to_state=to_state,
        count_args=func.__code__.co_argcount,
        func=func,
    )
