import pytest
import pytest_timeout
from pytest_assume.plugin import assume


class TestAssume(object):

    def test_01(self):
        a = 1
        b = 2
        assume(a == b)

    def test_02(self):
        a = 1
        b = 1
        assume(a == b)


if __name__ == '__main__':
    pytest.main(['-s'])

