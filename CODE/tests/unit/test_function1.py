import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../../src')))

from function1 import add_numbers

def test_add_numbers():
    assert add_numbers(2,3) == 5
    assert add_numbers(-1,1) == 0
    assert add_numbers(0,0) == 0
    