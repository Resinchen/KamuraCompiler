from collections import deque
from typing import TYPE_CHECKING, Any, cast

from lrparser.utils.exceptions import LRParserError
from lrparser.utils.parser import Action, ActionType, Attribute, Reduce, State
from lrparser.utils.table import ActionTable, GotoTable, Terminal
from lrparser.utils.tokenizer import Token

if TYPE_CHECKING:
    from lrparser.utils.parser import Shift


class Parser:
    def __init__(
        self,
        action_table: dict[str, dict[str, Any]],
        goto_table: dict[str, dict[str, Any]],
    ):
        self._actions = ActionTable(action_table)
        self._goto = GotoTable(goto_table)
        self._stack: list[State] = [State('DOWN')]

    def parse(self, tokens: list[Token]) -> Attribute | None:
        tokens_deque = deque(tokens)
        while len(tokens_deque):
            lookahead: Token = tokens_deque[0]
            current_state: State = self._stack.pop()
            cell: Action = self._actions.get(current_state, Terminal(lookahead.type.name))
            match cell.type:
                case ActionType.SHIFT:
                    self._stack.extend([current_state, cast('Shift', cell).execute(lookahead)])
                    tokens_deque.popleft()
                case ActionType.REDUCE:
                    self._stack.extend(self._execute_reduce(cast('Reduce', cell), current_state))
                case ActionType.FINISH:
                    return current_state.attributes.get('res')
                case _:
                    raise LRParserError(f'Unexpected state: {current_state}')
        return None

    def _execute_reduce(self, cell: Reduce, current_state: State) -> list[State]:
        reduce_args = [current_state] + [self._stack.pop() for _ in range(cell.count_args - 1)]
        reduce_args.reverse()
        reduced_state = cell.make_reduce(reduce_args)
        top_state = self._stack.pop()
        new_state_name = self._goto.get(top_state, reduced_state)
        return [top_state, State(new_state_name, reduced_state.attributes)]
