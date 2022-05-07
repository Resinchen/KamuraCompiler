import pytest
import re
from lrparser.utils.tokenizer import TokenType


class TokenTypeTest:
    def test_parse_json(self):
        assert TokenType.from_json({"name": "kek", "pattern": "kek"}) == TokenType(name='kek', pattern=re.compile('kek'))

    def test_parse_invalid_json(self):
        with pytest.raises(KeyError):
            TokenType.from_json({"name": "kek", "lol": "kek"})
