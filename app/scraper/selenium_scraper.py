from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

class SeleniumScraper:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.options = options

    def get_page(self, url):
        driver = webdriver.Chrome(service=self.service, options=self.options)
        driver.get(url)
        time.sleep(2)  # wait for JavaScript to load content
        html = driver.page_source
        driver.quit()
        return html
