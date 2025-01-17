import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../../src/integration')))

from database import init_db, add_user, get_user

@pytest.fixture
def db_connection():
    conn = init_db() 
    yield conn
    conn.close()
    
@pytest.mark.integration
def test_add_and_get_user(db_connection):
    user_id = add_user(db_connection, "Laura")
    user = get_user(db_connection, user_id)
    assert user == (1, "Laura")
    