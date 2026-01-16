from app.db.sqlite_database import SQLiteDB
from app.config import SQLITE_DB_PATH

db = SQLiteDB(SQLITE_DB_PATH)

rows = db.fetch_all()
print(f"Total rows: {len(rows)}")
for row in rows:
    print(row)

db.close()