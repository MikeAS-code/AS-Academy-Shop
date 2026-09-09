from web_driver import WebDriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import html
import config

def login(navegador, username, password):

    button = navegador.find_element(By.XPATH, '//a[contains(.,"Iniciar sesión")]').click()
    time.sleep(2)

    navegador.find_element(By.ID, 'username').send_keys(username)
    navegador.find_element(By.ID, 'password').send_keys(password)

    bot = navegador.find_element(By.ID, 'bot').click()

    button_submit = WebDriverWait(navegador, 10).until(
     EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="login-submit"]'))
    )
    button_submit.click()

    time.sleep(5)


def get_products(navegador):
    
    button_products = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//a[@href="/productos"]')
        )
    )

    button_products.click()

    time.sleep(5)

    html_products = navegador.page_source

    tree = html.fromstring(html_products)

    productos = tree.xpath('//div[@data-testid="product-card"]')

    return productos


if __name__ == "__main__":
    print("Start crawler")
  
    navegador = WebDriver()

    navegador.open_url(config.URL_BASE)

    time.sleep(5)

    login(navegador.get_driver(), config.USERNAME, config.PASSWORD)

    productos = get_products(navegador.get_driver())
    print(f"Total products found: {len(productos)}")

    print("End crawler")
