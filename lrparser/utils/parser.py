from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Sequence

from lrparser.utils.tokenizer import Token

_SimpleTypes = str | int | bool
Attribute = str | int | bool | list[_SimpleTypes]


class ActionType(int, Enum):
    SHIFT = 0
    REDUCE = 1
    FINISH = 2


@dataclass
class State:
    name: str
    attributes: dict[str, Attribute] = field(default_factory=dict)

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, State):
            return False
        return self.name == other.name

    def get(self, key: str) -> Attribute | None:
        return self.attributes.get(key)


@dataclass
class Shift:
    from_state: State
    to_state: State
    type: ActionType = ActionType.SHIFT

    def execute(self, lookahead: Token) -> State:
        new_state: State = self.to_state
        if lookahead.value:
            new_state.attributes['val'] = lookahead.value
        return new_state


@dataclass
class Finish:
    from_state: State
    to_state: State
    type: ActionType = ActionType.FINISH


@dataclass
class Reduce:
    from_state: State
    to_state: State
    count_args: int
    func: Callable[[State], dict[str, Attribute]]
    type: ActionType = ActionType.REDUCE

    def make_reduce(self, args: Sequence[State]) -> State:
        state = State(self.to_state.name)
        func_result = self.func(*args)
        state.attributes.update(func_result)

        return state


Action = Shift | Finish | Reduce
