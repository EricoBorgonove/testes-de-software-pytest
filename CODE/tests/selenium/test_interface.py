import time
from selenium import webdriver

def test_page_load():
    # cria uma instancia do wedriver para o navegador selecionado
    driver = webdriver.Chrome()
    # o driver carrega a página selecionada
    driver.get("https://www.google.com")
    #adiciona uma parada na execução (segundos)
    time.sleep(3)
    #fecha o webdriver
    assert "Google" in driver.title
    driver.quit()