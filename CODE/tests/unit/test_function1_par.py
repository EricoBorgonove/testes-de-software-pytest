import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../../src')))

from function1 import add_numbers

# Teste com parametros
@pytest.mark.parametrize("a, b, esperado", [
    (1,2,3),
    (5,6,11),
    (9,7,16)
])

def test_add_numbers(a, b, esperado):
    assert add_numbers(a, b) == esperado


