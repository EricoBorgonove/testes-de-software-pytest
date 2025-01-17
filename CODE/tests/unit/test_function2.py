import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../../src')))

from function2 import is_even


@pytest.mark.parametrize("number, esperado", [
    (20, True),
    (0, True),
    (63, False),
    (568, True),
    (7, False)
])

def test_is_even_parametrize(number, esperado):
    assert is_even(number) is esperado 

def test_is_even ():
    assert is_even(1) is not True
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(4) is True
    