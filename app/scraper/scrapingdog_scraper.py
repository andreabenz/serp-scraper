import requests

class ScrapingDogScraper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.scrapingdog.com/scrape"

    def get_page(self, url):
        """Fetch page using ScrapingDog API"""
        params = {
            "api_key": self.api_key,
            "url": url,
            "render": "true"  # Enable JavaScript rendering
        }
        
        try:
            print(f"[INFO] Fetching URL with ScrapingDog: {url}")
            response = requests.get(self.base_url, params=params, timeout=30)
            response.raise_for_status()
            
            print("[INFO] Page fetched successfully with ScrapingDog API")
            return response.text
        
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] ScrapingDog API error: {e}")
            raise Exception(f"Failed to fetch page with ScrapingDog: {e}")
