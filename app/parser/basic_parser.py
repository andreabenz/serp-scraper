from bs4 import BeautifulSoup

class BasicParser:
    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        results = []
        # Find the container for search results
        container = soup.find("div", {"class": "dURPMd"})
        if not container:
            return results
        allData = container.find_all("div", {"class": "Ww4FFb"})
        for item in allData:
            title_tag = item.find("h3")
            link_tag  = item.find("a")
            desc_tag  = item.find("div", {"class": "VwiC3b"})
            results.append({
                "title":       title_tag.text if title_tag else None,
                "link":        link_tag['href'] if link_tag else None,
                "description": desc_tag.text if desc_tag else None
            })
        return results
