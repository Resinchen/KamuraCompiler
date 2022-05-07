import operator

import pytest

from lrparser.utils.table import Terminal


class TerminalTest:
    @pytest.mark.parametrize(
        ('op', 'left', 'right'),
        [
            (operator.eq, Terminal('kek'), Terminal('kek')),
            (operator.ne, Terminal('kek'), Terminal('lol')),
        ]
    )
    def test_equals(self, op, left, right):
        assert op(left, right)

