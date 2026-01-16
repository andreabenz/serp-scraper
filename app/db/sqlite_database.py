import sqlite3
from datetime import datetime

class SQLiteDB:
    def __init__(self, db_path):
        self.conn   = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        # Create table if it does not exist already
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                position INTEGER,
                title TEXT,
                link TEXT,
                domain TEXT,
                description TEXT,
                description_length INTEGER,
                result_type TEXT,
                rating REAL,
                is_ad BOOLEAN,
                scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def insert_result(self, position=None, title=None, link=None, domain=None, description=None, description_length=None, result_type=None, rating=None, is_ad=False, scraped_at=None):
        if scraped_at is None:
            scraped_at = datetime.now()
        
        self.cursor.execute(
            """INSERT INTO results 
               (position, title, link, domain, description, description_length, result_type, rating, is_ad, scraped_at) 
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (position, title, link, domain, description, description_length, result_type, rating, is_ad, scraped_at)
        )
        self.conn.commit()

    def close(self):
        self.conn.close()

    def fetch_all(self):
        self.cursor.execute(
            """SELECT id, position, title, link, domain, description, 
                      description_length, result_type, rating, is_ad, scraped_at 
               FROM results"""
        )
        return self.cursor.fetchall()