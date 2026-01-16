from app.config import (
    SCRAPER,
    PARSER,
    DATABASE,
    CHROMEDRIVER_PATH,
    SEARCH_QUERY,
    SQLITE_DB_PATH,
)

# Initialize the chosen scraper
if SCRAPER == "selenium":
    from app.scraper.selenium_scraper import SeleniumScraper
    scraper = SeleniumScraper(CHROMEDRIVER_PATH)
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
    db.insert_result(item["title"], item["link"], item["description"])
db.close()                             # close the connection
