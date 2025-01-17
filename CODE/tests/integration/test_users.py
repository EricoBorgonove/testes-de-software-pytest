import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../../src/integration')))

from users import UserSystem

@pytest.fixture
def user_system():
    return UserSystem()

@pytest.mark.unit
def test_user_registration(user_system):
    #Teste Registro do Usuário
    result= user_system.register_user("Laura", "123456")
    assert result == "User registered"    

@pytest.mark.integration
def test_user_registration_and_autentication(user_system):
    #Teste Registro do Usuário
    result= user_system.register_user("Laura", "123456")
    assert result == "User registered"
    # Teste de Autenticação válida
    auth_result = user_system.authenticate_user("Laura", "123456")
    assert auth_result == "Authentication successful"
    # Teste de Autenticação inválida
    auth_result_fail = user_system.authenticate_user("Laura", "123")
    assert auth_result_fail == "Authentication failed"