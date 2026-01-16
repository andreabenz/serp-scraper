from bs4 import BeautifulSoup
from urllib.parse import urlparse

class BasicParser:
    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        results = []
        
        # Find the container for search results
        container = soup.find("div", {"class": "dURPMd"})
        if not container:
            return results
        
        allData = container.find_all("div", {"class": "Ww4FFb"})
        
        for position, item in enumerate(allData, start=1):
            title_tag = item.find("h3")
            link_tag = item.find("a")
            desc_tag = item.find("div", {"class": "VwiC3b"})
            
            # Extract URL and domain
            url = link_tag['href'] if link_tag else None
            domain = self._extract_domain(url) if url else None
            
            # Description and its length
            description = desc_tag.text if desc_tag else None
            description_length = len(description) if description else 0
            
            # Check if result is an ad
            is_ad = self._is_ad_result(item)
            
            # Extract rating if available (from rich snippets)
            rating = self._extract_rating(item)
            
            # Determine result type
            result_type = self._determine_result_type(item)
            
            results.append({
                "position": position,
                "title": title_tag.text if title_tag else None,
                "link": url,
                "domain": domain,
                "description": description,
                "description_length": description_length,
                "result_type": result_type,
                "rating": rating,
                "is_ad": is_ad
            })
        
        return results
    
    def _extract_domain(self, url):
        """Extract domain from URL"""
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.replace("www.", "")
            return domain
        except:
            return None
    
    def _is_ad_result(self, item):
        """Check if result is an ad by looking for ad indicators"""
        # Look for ad badge or sponsor labels
        ad_indicators = item.find_all(["span", "div"], string=lambda s: s and ("Ad" in s or "Sponsored" in s))
        return len(ad_indicators) > 0
    
    def _extract_rating(self, item):
        """Extract rating from rich snippets (e.g., star ratings)"""
        try:
            # Look for rating elements
            rating_element = item.find("span", {"role": "img"})
            if rating_element and "out of" in rating_element.get("aria-label", ""):
                # Parse "4.5 out of 5" format
                aria_label = rating_element.get("aria-label", "")
                rating_str = aria_label.split()[0]
                return float(rating_str)
        except:
            pass
        return None
    
    def _determine_result_type(self, item):
        """Determine the type of result (organic, featured_snippet, knowledge_panel, etc.)"""
        # Check for featured snippet indicators
        if item.find("div", {"class": "ifM9O"}):
            return "featured_snippet"
        
        # Check for knowledge panel
        if item.find("div", {"class": "kp-wholepage"}):
            return "knowledge_panel"
        
        # Check for video results
        if item.find("a", {"data-ved": True}) and item.find("img"):
            if "youtube" in str(item).lower():
                return "video"
        
        # Default to organic
        return "organic"
