from selenium import webdriver

class WebDriver:

    def __init__(self):
        self._navegador = webdriver.Chrome()

    def open_url(self, url):
        self._navegador.get(url)

    def get_html(self):
        return self._navegador.page_source

    def get_driver(self):
        return self._navegador

    def close(self):
        self._navegador.quit()