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
        
        # Migrate old schema to new schema
        self._migrate_schema()

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

    def _migrate_schema(self):
        """Add missing columns from old schema to new schema"""
        # Get existing columns
        self.cursor.execute("PRAGMA table_info(results)")
        existing_columns = {row[1] for row in self.cursor.fetchall()}
        
        # Define new columns and their definitions (without CURRENT_TIMESTAMP for migration)
        new_columns = {
            "position": "INTEGER",
            "domain": "TEXT",
            "description_length": "INTEGER",
            "result_type": "TEXT",
            "rating": "REAL",
            "is_ad": "BOOLEAN",
            "scraped_at": "TIMESTAMP"
        }
        
        # Add missing columns
        for column, column_type in new_columns.items():
            if column not in existing_columns:
                try:
                    self.cursor.execute(f"ALTER TABLE results ADD COLUMN {column} {column_type}")
                    print(f"[MIGRATION] Added column: {column}")
                except sqlite3.OperationalError as e:
                    print(f"[MIGRATION] Error adding column {column}: {e}")
        
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute(
            """SELECT id, position, title, link, domain, description, 
                      description_length, result_type, rating, is_ad, scraped_at 
               FROM results"""
        )
        return self.cursor.fetchall()