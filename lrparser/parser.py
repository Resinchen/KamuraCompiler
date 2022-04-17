from collections import deque
from typing import cast

from lrparser.utils.exceptions import LRParserError
from lrparser.utils.parser import Action, Attribute, Finish, Reduce, Shift, State
from lrparser.utils.table import ActionTable, GotoTable, Terminal
from lrparser.utils.table_descriptor import ActionTableDescriptor, GotoTableDescriptor
from lrparser.utils.tokenizer import Token


class Parser:
    def __init__(
        self,
        action_descriptor: ActionTableDescriptor,
        goto_descriptor: GotoTableDescriptor,
    ):
        self._actions = ActionTable(action_descriptor)
        self._goto = GotoTable(goto_descriptor)
        self._stack: list[State] = [State("DOWN")]

    def parse(self, tokens: list[Token]) -> Attribute:
        tokens = deque(tokens)
        while len(tokens):
            lookahead: Token = tokens[0]
            current_state: State = self._stack.pop()
            cell: Action = self._actions.get(
                current_state, Terminal(lookahead.type.name)
            )
            if isinstance(cell, Shift):
                cell = cast(Shift, cell)
                new_state: State = cell.to_state
                if lookahead.value:
                    new_state.attributes["val"] = lookahead.value
                self._stack.append(current_state)
                self._stack.append(new_state)
                tokens.popleft()
            elif isinstance(cell, Reduce):
                cell: Reduce = cast(Reduce, cell)
                reduce_args = [current_state] + [
                    self._stack.pop() for _ in range(cell.count_args - 1)
                ]
                reduce_args.reverse()
                reduced_state = cell.make_reduce(reduce_args)
                top_state = self._stack.pop()
                new_state_name = self._goto.get(top_state, reduced_state)
                new_state = State(new_state_name, reduced_state.attributes)
                self._stack.append(top_state)
                self._stack.append(new_state)
            elif isinstance(cell, Finish):
                return current_state.attributes.get("res")
            else:
                raise LRParserError(f"Unexpected state: {current_state}")
