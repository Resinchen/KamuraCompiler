import re

import pytest

from lrparser.tokenizer import Tokenizer
from lrparser.utils.tokenizer import Token, TokenType

TOKEN_TYPES = {
    "kek": TokenType(name="kek", pattern=re.compile("kek")),
    "lol": TokenType(name="lol", pattern=re.compile("lol")),
    "none": TokenType(name="none", pattern=re.compile("[ \n]+")),
    "eof": TokenType(name="eof", pattern=re.compile("")),
}


@pytest.fixture()
def tokenizer() -> Tokenizer:
    return Tokenizer(list(TOKEN_TYPES.values()))


class TokenizerTest:
    def test_tokenize(self, tokenizer):
        expected_tokens = [
            Token(TOKEN_TYPES["lol"], value="lol"),
            Token(TOKEN_TYPES["none"], value=" "),
            Token(TOKEN_TYPES["kek"], value="kek"),
            Token(TOKEN_TYPES["none"], value="    \n"),
            Token(TOKEN_TYPES["kek"], value="kek"),
            Token(TOKEN_TYPES["eof"], value="eof"),
        ]
        text = "lol kek    \nkek"

        assert tokenizer.tokenize(text) == expected_tokens
