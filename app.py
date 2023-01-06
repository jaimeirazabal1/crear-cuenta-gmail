from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Crea una opción de Chrome para iniciar en modo incógnito
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Abre Google Chrome en modo incógnito
driver = webdriver.Chrome(chrome_options=chrome_options)

# Accede a la página web de Google
driver.get("https://www.google.com")
print(driver.page_source)
# Encuentra el botón "Acceder" y haz clic en él
button = driver.find_element_by_link_text("Acceder")
button.click()
logs = driver.get_log("browser")
for log in logs:
    print(log)

# Espera a que el usuario presione "Enter" antes de finalizar el proceso
input()
