from dataclasses import dataclass, field
from typing import Callable

from lrparser.utils.tokenizer import Token

_SimpleTypes = str | int | bool
Attribute = _SimpleTypes | list[_SimpleTypes]


@dataclass
class State:
    name: str
    attributes: dict[str, Attribute] = field(default_factory=dict)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def get(self, key: str) -> Attribute:
        return self.attributes.get(key)


@dataclass
class Shift:
    from_state: State
    to_state: State
    type: str = "SHIFT"

    def execute(self, lookahead: Token) -> State:
        new_state: State = self.to_state
        if lookahead.value:
            new_state.attributes["val"] = lookahead.value
        return new_state


@dataclass
class Finish:
    from_state: State
    to_state: State
    type: str = "FINISH"


@dataclass
class Reduce:
    from_state: State
    to_state: State
    count_args: int
    func: Callable[[list[State]], dict[str, Attribute]]
    type: str = "REDUCE"

    def make_reduce(self, args: list[State]) -> State:
        state = State(self.to_state.name)
        func_result = self.func(*args)
        state.attributes.update(func_result)

        return state


Action = Shift | Finish | Reduce
