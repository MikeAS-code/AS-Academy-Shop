from web_driver import WebDriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import html
import config
import random

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

    time.sleep(2)


def get_products(navegador):

    products = []
    
    html_products = navegador.page_source

    tree = html.fromstring(html_products)

    card_products = tree.xpath('//div[@data-testid="product-card"]')

    for card in card_products:
        try:
            title = card.xpath('.//h3[@data-testid="product-title"]/text()')[0]
            if not title:
                title = " "
        except Exception as e:
            title = " "

        try:
            price = card.xpath('.//span[@data-testid="product-price"]/text()')[0]
            if not price:
                price = 0
        except Exception as e:
            price = 0

        try:
            category = card.xpath('.//span[@data-testid="product-category"]/text()')[0]
            if not category:
                category = " "
        except Exception as e:
            category = " "

        try:
            description = card.xpath('.//p[@data-testid="product-description"]/text()')[0]
            if not description:
                description = " "
        except Exception as e:
            description = " "

        try:
            availability = card.xpath('.//span[@data-testid="product-status"]/text()')[0]
            if not availability:
                availability = " "
        except Exception as e:
            availability = " "

        try:
            image = card.xpath('.//img[@data-testid="product-card-image"]/@src')[0]
            if not image:
                image = " "
        except Exception as e:
            image = " "

        products.append({
            'title': title,
            'price': price,
            'category': category,
            'description': description,
            'availability': availability,
            'image': image
        })
    return products

def cargar_reviews(navegador):

    # Cantidad de productos de la página actual
    botones = navegador.find_elements(
        By.XPATH,
        '//button[@data-testid="product-detail-button"]'
    )

    total = len(botones)

    print(f"Productos encontrados: {total}")

    for i in range(total):

        print(f"Procesando producto {i + 1}/{total}")

        boton_ver_detalle = botones[i]

          # Llevar el botón al centro de la pantalla
        navegador.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            boton_ver_detalle
        )

        boton_ver_detalle.click()

        time.sleep(4)

        name_product = navegador.find_element(
            By.XPATH,
            '//h2'
        ).text

        price_product = navegador.find_element(By.XPATH, '//h2/following-sibling::p[1]').text.replace("$", "")

        texto_review = f"La verdad que el producto {name_product} cumple con mis expectativas, su precio {price_product} totalmente accesible. Recomiendo este producto."

        navegador.find_element(By.XPATH, '//input[@data-testid="comment-name"]').send_keys(config.nombres[random.randint(0, len(config.nombres) - 1)])

        rating = random.choice(["3", "4", "5"])

        select = Select(
                navegador.find_element(
                By.CSS_SELECTOR,
                'select[data-testid="comment-rating"]'
            )
        )

        select.select_by_value(rating)

        navegador.find_element(By.XPATH, '//textarea[@data-testid="comment-text"]').send_keys(texto_review)

        time.sleep(5)

        boton_cerrar_modal = navegador.find_element(
            By.XPATH,
            '//button[@aria-label="Cerrar modal"]'
        )
        boton_cerrar_modal.click()
        time.sleep(2)

def get_total_pages(navegador):

    elemento = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//div[starts-with(normalize-space(.), "Página")]'
            )
        )
    )

    texto = elemento.text

    print("Texto encontrado:", texto)

    total_paginas = int(texto.split("de")[-1].strip())

    return total_paginas


def next_page(navegador):

    boton_siguiente = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[@data-testid="pagination-next"]')
        )
    )

    boton_siguiente.click()

    time.sleep(2)

def go_to_products(navegador):

    button_products = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//a[@href="/productos"]')
        )
    )

    button_products.click()

    time.sleep(5)


if __name__ == "__main__":
    print("Start crawler")
  
    navegador = WebDriver()

    navegador.open_url(config.URL_BASE)

    time.sleep(5)

    login(navegador.get_driver(), config.USERNAME, config.PASSWORD)

    go_to_products(navegador.get_driver())

    total_paginas = get_total_pages(navegador.get_driver())

    print(f"Total de páginas: {total_paginas}")

    products = []

    for pagina in range(total_paginas):

        print(f"Procesando página {pagina + 1} de {total_paginas}")

        nuevos_productos = get_products(navegador.get_driver())

        products.extend(nuevos_productos)

        cargar_reviews(navegador.get_driver())

        if pagina < total_paginas - 1:
            next_page(navegador.get_driver())

    print(f"Total products found: {len(products)}")

    ##Aqui va el procesamiento de los productos, como guardarlos en un archivo o base de datos


    print("End crawler")
