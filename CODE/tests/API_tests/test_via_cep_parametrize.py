from urllib import response
import pytest
import requests

@pytest.mark.parametrize("cep, expected_city, expected_uf ", [
    ("01001-000", "São Paulo", "SP"),
    ("30140-071", "Belo Horizonte", "MG"),
    ("70040-010", "Brasília", "DF")
])

@pytest.mark.api_via_cep
def test_multiple_cep (cep, expected_city, expected_uf):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["localidade"] == expected_city
    assert data["uf"] == expected_uf
    
@pytest.mark.api_via_cep
def test_invalid_cep():
    invalid_cep = "69010999"
    url = f"https://viacep.com.br/ws/{invalid_cep}/json/"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    
    assert "erro" in data
    assert data["erro"] == "true"
    
@pytest.mark.api_via_cep
def test_incorrect_cep():
    incorrect_cep = "6901099"
    url = f"https://viacep.com.br/ws/{incorrect_cep}/json/"
    
    response = requests.get(url)
    assert response.status_code == 400
    
    assert "Bad Request" in response.text