import sqlite3

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
                title TEXT,
                link TEXT,
                description TEXT
            )
        """)
        self.conn.commit()

    def insert_result(self, title, link, description):
        self.cursor.execute(
            "INSERT INTO results (title, link, description) VALUES (?, ?, ?)",
            (title, link, description)
        )
        self.conn.commit()

    def close(self):
        self.conn.close()

    def fetch_all(self):
        self.cursor.execute(
            "SELECT id, title, link, description FROM results"
        )
        return self.cursor.fetchall()