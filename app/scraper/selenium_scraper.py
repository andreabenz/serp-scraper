from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.config import SCREENSHOT_PATH
import time
import os

class SeleniumScraper:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")  # Run in headless mode (turn off for debugging)
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("--disable-blink-features=AutomationControlled")

    def get_page(self, url):
        driver = webdriver.Chrome(service=self.service, options=self.options)
        
        driver.get(url)

        time.sleep(2)

        # --- COOKIE-BANNER ÜBERWINDEN 
        try:                 
            wait = WebDriverWait(driver, 5)
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "L2AGLb")))
            cookie_button.click()                
            print("[INFO] Cookie-Banner erfolgreich akzeptiert.")                 
            time.sleep(2)
        except Exception as e:
            print(f"[INFO] Cookie-Banner nicht gefunden oder nicht klickbar: {e}")

        page_html = driver.page_source

        # Screenshot der letzten Ansicht speichern
        os.makedirs(os.path.dirname(SCREENSHOT_PATH), exist_ok=True) if os.path.dirname(SCREENSHOT_PATH) else None
        driver.save_screenshot(SCREENSHOT_PATH)
        print(f"Screenshot gespeichert unter: {SCREENSHOT_PATH}")

        driver.quit()
        
        return page_html