import re
from dataclasses import dataclass
from re import Pattern


@dataclass
class TokenType:
    name: str
    pattern: Pattern[str]

    @classmethod
    def from_json(cls, data: dict[str, str]) -> 'TokenType':
        compile_pattern = re.compile(data['pattern'])
        return cls(name=data['name'], pattern=compile_pattern)


@dataclass
class Token:
    type: TokenType
    value: str
