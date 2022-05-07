import re

import pytest

from lrparser.tokenizer import Tokenizer
from lrparser.utils.tokenizer import TokenType


@pytest.fixture()
def tokenizer() -> Tokenizer:
    return Tokenizer([
        TokenType(name='kek', pattern=re.compile('kek')),
        TokenType(name='lol', pattern=re.compile('lol')),
        TokenType(name='open', pattern=re.compile('{')),
        TokenType(name='close', pattern=re.compile('}')),
        TokenType(name='none', pattern=re.compile('[ \n\t]+')),
    ])

class TokenizerTest:
    ...
