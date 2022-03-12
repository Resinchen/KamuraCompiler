from dataclasses import dataclass, field
from typing import Callable, Union

_SimpleTypes = Union[str, int, bool]
Attribute = Union[_SimpleTypes, list[_SimpleTypes]]


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


Action = Union[Shift, Finish, Reduce]
