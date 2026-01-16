from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env into environment

# Paths and queries from environment
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH")
SEARCH_QUERY     = os.getenv("SEARCH_QUERY")
SQLITE_DB_PATH   = os.getenv("SQLITE_DB_PATH", "results.db")

# Component selectors (choose which implementation to use)
SCRAPER  = os.getenv("SCRAPER", "selenium")
PARSER   = os.getenv("PARSER", "basic_parser")
DATABASE = os.getenv("DATABASE", "sqlite")