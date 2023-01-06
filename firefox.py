from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from faker import Faker
import random

fake = Faker()



# Crea una opción de Firefox para iniciar en modo incógnito
firefox_options = Options()
firefox_options.add_argument("--private")

# Abre Mozilla Firefox en modo incógnito
driver = webdriver.Firefox(options=firefox_options)

# Accede a la página web de Google
driver.get("https://www.google.com")

# Encuentra el botón "Acceder" y haz clic en él
button = driver.find_element("link text","Iniciar sesión")
button.click()

# Encuentra el botón "Acceder" y haz clic en él
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Crear cuenta']"))).click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Para mi uso personal']"))).click()

first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
username = fake.user_name()
password = fake.password()

chars = "abcdefghijklmnopqrstuvwxyz0123456789"
id_length = 6
random_id = "".join(random.choices(chars, k=id_length))

driver.find_element("id","firstName").send_keys(first_name)
driver.find_element("id","lastName").send_keys(last_name)
driver.find_element("id","username").send_keys(username+random_id)
driver.find_element("name","Passwd").send_keys(password)
driver.find_element("name","ConfirmPasswd").send_keys(password)

wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Siguiente']"))).click()



