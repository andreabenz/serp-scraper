from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

# Set path to ChromeDriver (Replace this with the correct path)
CHROMEDRIVER_PATH = "C:\\Users\\andre\\OneDrive - TBZ\\TBZ\\M122 - Skriptsprache\\chromedriver-win64\\chromedriver.exe"
# Initialize WebDriver with Service
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()


options.add_argument("--window-size=1920,1080")  # Set window size
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=service, options=options)

# Open Google Search URL
search_url = "https://www.google.com/search?q=lead+generation+tools&oq=lead+generation+tools"

driver.get(search_url)

# Wait for the page to load
time.sleep(2)

page_html = driver.page_source
print(page_html)