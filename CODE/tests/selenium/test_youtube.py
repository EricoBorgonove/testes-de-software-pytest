from selenium import webdriver
# importa a biblioteca de métodos para encontar os elementos
from selenium.webdriver.common.by import By 
import pytest
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

driver.find_element(By.NAME, "search_query").send_keys("Ana Paula Valadão")
driver.find_element(By.CLASS_NAME, "ytSearchboxComponentSearchButton").click()
time.sleep(3)

assert "search_query=Ana+Paula+Valad%C3%A3o" in driver.current_url
assert "Ana Paula Valadão" in driver.title


#time.sleep(3)
driver.quit()

#https://www.youtube.com/results?search_query=Ana+Paula+Valad%C3%A3o