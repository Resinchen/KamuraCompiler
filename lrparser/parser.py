from collections import deque
from typing import cast

from lrparser.utils.action_table_descriptor import ActionTableDescriptor
from lrparser.utils.exceptions import LRParserError
from lrparser.utils.goto_table_descriptor import GotoTableDescriptor
from lrparser.utils.parser import Action, Attribute, Reduce, State
from lrparser.utils.table import ActionTable, GotoTable, Terminal
from lrparser.utils.tokenizer import Token


class Parser:
    def __init__(
        self,
        action_descriptor: ActionTableDescriptor,
        goto_descriptor: GotoTableDescriptor,
    ):
        self._actions = ActionTable(action_descriptor)
        self._goto = GotoTable(goto_descriptor)
        self._stack: list[State] = [State('DOWN')]

    def parse(self, tokens: list[Token]) -> Attribute:
        tokens = deque(tokens)
        while len(tokens):
            lookahead: Token = tokens[0]
            current_state: State = self._stack.pop()
            cell: Action = self._actions.get(
                current_state, Terminal(lookahead.type.name)
            )
            match cell.type:
                case 'SHIFT':
                    self._stack.extend([current_state, cell.execute(lookahead)])
                    tokens.popleft()
                case 'REDUCE':
                    self._stack.extend(
                        self._execute_reduce(cast(Reduce, cell), current_state)
                    )
                case 'FINISH':
                    return current_state.attributes.get('res')
                case _:
                    raise LRParserError(f'Unexpected state: {current_state}')

    def _execute_reduce(
        self, cell: Reduce, current_state: State
    ) -> list[State]:
        reduce_args = [current_state] + [
            self._stack.pop() for _ in range(cell.count_args - 1)
        ]
        reduce_args.reverse()
        reduced_state = cell.make_reduce(reduce_args)
        top_state = self._stack.pop()
        new_state_name = self._goto.get(top_state, reduced_state)
        return [top_state, State(new_state_name, reduced_state.attributes)]
