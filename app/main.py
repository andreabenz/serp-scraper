from app.config import (
    SCRAPER,
    PARSER,
    DATABASE,
    CHROMEDRIVER_PATH,
    SEARCH_QUERY,
    SQLITE_DB_PATH,
    SCRAPINGDOG_API_KEY,
)

# Initialize the chosen scraper
if SCRAPER == "selenium":
    from app.scraper.selenium_scraper import SeleniumScraper
    scraper = SeleniumScraper(CHROMEDRIVER_PATH)
elif SCRAPER == "scrapingdog":
    from app.scraper.scrapingdog_scraper import ScrapingDogScraper
    scraper = ScrapingDogScraper(SCRAPINGDOG_API_KEY)
else:
    raise ValueError(f"Unknown scraper: {SCRAPER}")

# Initialize the chosen parser
if PARSER == "basic_parser":
    from app.parser.basic_parser import BasicParser
    parser = BasicParser()
else:
    raise ValueError(f"Unknown parser: {PARSER}")

# Initialize the chosen database
if DATABASE == "sqlite":
    from app.db.sqlite_database import SQLiteDB
    db = SQLiteDB(SQLITE_DB_PATH)
else:
    raise ValueError(f"Unknown database: {DATABASE}")

# Run the process once
url = f"https://www.google.com/search?q={SEARCH_QUERY}"
html = scraper.get_page(url)            # scrape the search results page
data = parser.parse(html)              # parse into structured data

# Save results to the database
for item in data:
    db.insert_result(
        position=item["position"],
        title=item["title"],
        link=item["link"],
        domain=item["domain"],
        description=item["description"],
        description_length=item["description_length"],
        result_type=item["result_type"],
        rating=item["rating"],
        is_ad=item["is_ad"]
    )
db.close()