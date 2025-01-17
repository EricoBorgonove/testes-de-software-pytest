import os
import sys
from urllib import response
import pytest
from flask import Flask

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../../src/integration')))

from py_flask import app as flask_app

@pytest.fixture
def client ():
    flask_app.testing = True
    with flask_app.test_client() as client:
        yield client

@pytest.mark.integration
def test_get_existing_user (client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json == {"name": "Taiana"}
    
@pytest.mark.integration
def test_get_non_existing_user (client):
    response = client.get("/users/3")
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}