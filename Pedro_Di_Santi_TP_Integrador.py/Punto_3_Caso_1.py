#Automatizar los siguientes casos de prueba. Luego de que sean automatizados,
#deben ser subidos a un repositorio git, se debe generar el archivo y debe retornar
#un reporte HTML con los resultados de la ejecución.


# Caso 1
# ● El usuario se loguea al sitio como usuario standard user
# ● Ordenar los elementos por “price (low to high)”
# ● Verificar que los elementos estén ordenados

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import pytest

def test_automatizado(driver):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    
    # El usuario se loguea al sitio como usuario standard user

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Ordenar los elementos por “price (low to high)”

    driver.get("https://www.saucedemo.com/inventory.html")
    driver.minimize_window()

    combo=Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    combo.select_by_visible_text("Price (low to high)")

    # Verificar que los elementos estén ordenados.


    elementos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    # Extraemos los precios como float

    precios = [float(e.text.replace("$", "")) for e in elementos]
    print()
    print("Precios extraídos:", precios)
    print()

    if precios == sorted(precios):
        print("Los productos están ordenados")
    else:
        print("Los productos NO están ordenados")
    print()
    print("Caso 1 Terminado")


