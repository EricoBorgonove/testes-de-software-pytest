import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../../src')))

from function4 import factorial

def test_factorial():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(0) == 1
    
    with pytest.raises(ValueError, match= "Número deve ser não-negativo."):
        factorial(-1)
        factorial(-30)