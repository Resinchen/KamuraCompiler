import re
from re import Match

from lrparser.utils.exceptions import LRSyntaxError
from lrparser.utils.tokenizer import Token, TokenType


class Tokenizer:
    def __init__(self, token_types: list[TokenType]):
        self.current_pos: int = 0
        self.token_types: list[TokenType] = token_types

    def tokenize(self, text: str) -> list[Token]:
        tokens: list[Token] = []
        while text[self.current_pos :] != "":
            candidate = self._get_token(text[self.current_pos :])
            tokens.append(candidate)

        return [
            token for token in tokens if token.type.name not in ["None", "comment"]
        ] + [Token(TokenType("eof", re.compile("")), "eof")]

    def _get_token(self, sub_string: str) -> Token:
        for token in self.token_types:
            result: Match = token.pattern.match(sub_string)
            if result:
                value = result.group(0)
                self.current_pos += len(value)

                return Token(token, value)
        else:
            raise LRSyntaxError(f"Can`t get token by pos {self.current_pos}")
