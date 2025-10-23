# Caso 2
#● El usuario se loguea al sitio como usuario standard user
#● Incorporar al carrito todos los elementos
#● Ir al carrito
#● Verificar que todos los elementos estén en el carrito
#● Ir al checkout
#● Ingresar nombre y clickear “Continue”
#● Verificar que aparece el error “Error: Last Name is required”
#● Ingresar un apellido y clickear “Continue”
#● Verificar que aparece el error “Error: Postal Code is required”

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
import pytest

@pytest.fixture

def driver():

    chrome_options=Options()
    driver = webdriver.Chrome(options=chrome_options)
    

    yield driver
    driver.quit()


def test_automatizado2(driver):
    
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

    # Incorporar al carrito todos los elementos
    # https://www.saucedemo.com/inventory.html


    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

    print()
    print("Se cargaron todos los articulos al carrito")
    print()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # https://www.saucedemo.com/cart.html

    # Verificar que todos los elementos estén en el carrito
    
    exito1=driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div").text 
    assert 'Sauce Labs Onesie' in exito1
    exito2=driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text 
    assert 'Sauce Labs Bike Light' in exito2
    exito3=driver.find_element(By.XPATH, "//*[@id='item_1_title_link']/div").text 
    assert 'Sauce Labs Bolt T-Shirt' in exito3
    exito4=driver.find_element(By.XPATH, "//*[@id='item_3_title_link']/div").text 
    assert 'Test.allTheThings() T-Shirt (Red)' in exito4
    exito5=driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").text 
    assert 'Sauce Labs Backpack' in exito5
    exito6=driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div").text 
    assert 'Sauce Labs Fleece Jacket' in exito6
    print()
    print("VALIDAMOS: Estan todos los articulos en el carrito")
    print()

    # Ir al checkout  
       
    
 
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@data-test='checkout']")))
    time.sleep(10)
    driver.find_element(By.XPATH,"//button[@data-test='checkout']").click()
  

    # Ingresar nombre y clickear “Continue”
    # Verificar que aparece el error “Error: Last Name is required”
    # Ingresar un apellido y clickear “Continue”
    # Verificar que aparece el error “Error: Postal Code is required”

    # https://www.saucedemo.com/checkout-step-one.html

#    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "firstName")))

    

    time.sleep(5)

    chrome_options.add_argument("--disable-features=TranslateUI,PasswordLeakDetection,PasswordManager")
    driver.find_element(By.ID, "first-name").send_keys("Peter")
   
    driver.find_element(By.ID, "continue").click()




    mensaje_error1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))).text 
    assert 'Error: Last Name is required' in mensaje_error1

    print()
    print("Last Name es Requerido")
    print()

    driver.find_element(By.ID,"last-name").send_keys("PruebaQA")
    driver.find_element(By.ID,"continue").click()

    mensaje_error2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))).text
    assert 'Error: Postal Code is required' in mensaje_error2

    print()
    print("Postal Code es Requerido")
    print("Caso 2 Terminado")
