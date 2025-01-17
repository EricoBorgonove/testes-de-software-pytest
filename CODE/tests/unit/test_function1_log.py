import sys
import os
from venv import logger
import pytest
import logging

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../../src')))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from function1 import add_numbers

def test_add_numbers():
    logger.info("Testando a soma de 0, 0")
    assert add_numbers(0, 0) == 0
    logger.info("Testando a soma de -1, 1")
    assert add_numbers(-1, 1) == 0
    logger.info("Testando a soma de 2, 3")
    assert add_numbers(2, 3) == 5


