# Caso 3
# El usuario se loguea al sitio como usuario standard user
# Agregar un elemento al carrito
# Ir al carrito
# Remover el artículo
# Verificar que el sitio no tiene artículos agregados
# Ir a “Continue Shopping”
# Agregar 2 elementos
# Ir al carrito
# Verificar que los elementos existan
# Hacer el checkout
# Finalizar la compra
# Verificar que la compra fue realizada

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import time
import pytest

@pytest.fixture

def driver():

    chrome_options=Options()
    driver = webdriver.Chrome(options=chrome_options)
    

    yield driver
    driver.quit()



def test_automatizado3(driver):
    
    chrome_options=Options()
    chrome_options.add_experimental_option("prefs", {
    "profile.password_manager_leak_detection": False
  })
    


    driver = webdriver.Chrome(options=chrome_options)



    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()


# El usuario se loguea al sitio como usuario standard user

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Agregar un elemento al carrito -- https://www.saucedemo.com/inventory.html
    time.sleep(3)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    time.sleep(3)
    print()
    print("Se cargo el articulo al carrito")
    print()

    # Ir al carrito y remover el artículo
    driver.find_element(By.ID, "shopping_cart_container").click()

    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    # Verificar que el sitio no tiene artículos agregados

    assert len(driver.find_elements(By.ID, "cart_item")) == 0, "No esta vacío"

    print()
    print("Validamos que esta vacio el carrito")
    print()

    # Ir a “Continue Shopping”

    driver.find_element(By.ID, "continue-shopping").click()

    # Agregar 2 elementos

    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()

    # Ir al carrito

    driver.find_element(By.ID, "shopping_cart_container").click()

    # Verificar que los elementos existan

    validacion1=driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div").text 
    assert 'Sauce Labs Bolt T-Shirt' in validacion1
    validacion2=driver.find_element(By.XPATH, "//*[@id='item_3_title_link']/div").text 
    assert 'Test.allTheThings() T-Shirt (Red)' in validacion2

    print()
    print("Validamos que hay 2 articulos en el carrito")
    print()

    # Hacer el checkout

    driver.find_element(By.ID, "checkout").click()

    # Finalizar la compra

    driver.find_element(By.ID, "first-name").send_keys('Peter')
    driver.find_element(By.ID, "last-name").send_keys('Di Santi')
    driver.find_element(By.ID, "postal-code").send_keys('4444')
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()


    # Verificar que la compra fue realizada

    exito=driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']/h2").text
    assert 'Thank you for your order!' in exito

    print()
    print("Compra finalizada y validada")
    print("Caso 3 Terminado")
