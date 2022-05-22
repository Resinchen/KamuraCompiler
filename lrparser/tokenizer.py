import re
from re import Match

from lrparser.utils.exceptions import LRSyntaxError
from lrparser.utils.tokenizer import Token, TokenType


class Tokenizer:
    def __init__(self, token_types: list[TokenType]):
        self._current_position: int = 0
        self._token_types: list[TokenType] = token_types

    def tokenize(self, text: str) -> list[Token]:
        text = text.replace('    ', '\t')
        tokens: list[Token] = []
        while text[self._current_position :] != "":
            candidate = self._get_token(text[self._current_position :])
            if candidate.type.name in ("None", "comment"):
                continue
            tokens.append(candidate)
        tokens.extend([Token(TokenType("end", re.compile("")), "end"), Token(TokenType("eof", re.compile("")), "eof")])

        return tokens

    def _get_token(self, sub_string: str) -> Token:
        for token in self._token_types:
            result: Match = token.pattern.match(sub_string)
            if result:
                value = result.group(0)
                self._current_position += len(value)

                return Token(token, value)
        else:
            raise LRSyntaxError(
                f"Can`t get token by pos {self._current_position}"
            )
