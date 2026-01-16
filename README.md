### SERP Scraper (Google)

> **Note:** This project was mostly created using AI.

Lightweight Python project to scrape a Google Search results page (SERP), parse core fields (position, title, link, domain, description, type, rating, ad), and persist them to a SQLite database. Includes optional screenshot capture and utilities to inspect, export, and clear stored results.

This repository is configured to use one of two scraping strategies:
- Selenium + Chrome/Chromedriver (default)
- ScrapingDog API (headless rendering via API)


### Stack
- Language: `Python`
- Frameworks/Libraries:
  - `selenium` (default scraper)
  - `beautifulsoup4` (HTML parsing)
  - `python-dotenv` (environment variable loading)
  - `requests` (required when using ScrapingDog API)
  - Database: `SQLite` (via Python stdlib `sqlite3`)

### Requirements
- Python 3.10+ (recommended)
- One of the scraping backends:
  - Selenium backend:
    - Google Chrome installed
    - Chromedriver binary compatible with your Chrome version
  - ScrapingDog backend:
    - ScrapingDog API key
- Internet connectivity


### Setup
1) Create and activate a virtual environment (recommended)
```bash
python -m venv .venv
python -m app.db.export_and_clear
```

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) Create a `.env` file (see the example above) and set required variables.


### Running the scraper
- Using the package module path (recommended):
```bash
python -m app.main
```

Behavior:
1) The selected scraper fetches a Google SERP for `SEARCH_QUERY`.
2) The parser extracts fields into structured records.
3) Records are inserted into the configured SQLite database.
4) If using Selenium, a screenshot is saved to `SCREENSHOT_PATH`.


### Utilities (Scripts)
- Print all rows in the database:
```bash
python -m app.db.read_results
```

- Export all rows to JSON and clear the table:
```bash
python -m app.db.export_and_clear
```
Exports are written to `EXPORT_PATH` (default `Data/exports`) with a timestamped filename.


### Known limitations
- Google SERP structure evolves; parsing selectors may need maintenance.
- Rate limits, captchas, and ToS considerations apply.
- If you run into I am not a robot captchas with selenium, you need to turn off headless mode and solve them manually.
- You might get IP-banned if you run the selenium scraper too frequently.