import json
from typing import cast

from lrparser.utils.table_descriptor import (
    ActionColumnDescriptor,
    ActionTableDescriptor,
    GotoTableDescriptor,
)
from lrparser.utils.tokenizer import TokenType


def reader_config(filepath: str) -> dict:
    with open(filepath, "r") as f:
        return json.load(f)


def parse_tokens(data) -> list[TokenType]:
    tokens = [TokenType.from_json(token) for token in data["tokens"]]
    return tokens


def parse_actions(data, funcs: dict) -> ActionTableDescriptor:
    actions = ActionTableDescriptor.from_json(data["actions"])
    for action_row in actions.rows:
        for action in action_row.items:
            if cast(ActionColumnDescriptor, action).func:
                cast(ActionColumnDescriptor, action).func = funcs[
                    cast(ActionColumnDescriptor, action).func
                ]

    return actions


def parse_goto(data) -> GotoTableDescriptor:
    goto = GotoTableDescriptor.from_json(data["goto"])
    return goto
