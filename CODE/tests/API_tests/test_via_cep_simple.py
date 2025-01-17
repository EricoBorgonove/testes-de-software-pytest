import requests
import pytest

@pytest.mark.api_via_cep
def test_valid_cep():
    url = "https://viacep.com.br/ws/69010100/json/"
    response = requests.get(url)
    
    assert response.status_code == 200, "Status code não é 200"
    data = response.json()   # converte o json em dicionário
    
    assert data["cep"] == "69010-100", "O Cep não é 69010-100"
    assert data["logradouro"] == "Rua Luiz Antony", "Não é a rua Luiz Antony"
    
    except_fields = ["cep", "logradouro", "localidade", "bairro"] # cria um dicionário com as chaves que serão testadas

    for field in except_fields:
        assert field in data, f"O campo {field}, não está presente"
        assert isinstance(data[field], (str, type(None)))
    