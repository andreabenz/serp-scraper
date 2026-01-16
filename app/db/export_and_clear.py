from app.db.sqlite_database import SQLiteDB
from app.config import SQLITE_DB_PATH, EXPORT_PATH
import json
import os
from datetime import datetime

db = SQLiteDB(SQLITE_DB_PATH)

# Fetch all results
rows = db.fetch_all()

if not rows:
    print("[INFO] No data to export. Database is empty.")
else:
    # Create export directory if it doesn't exist
    os.makedirs(EXPORT_PATH, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"search_results_{timestamp}.json"
    filepath = os.path.join(EXPORT_PATH, filename)
    
    # Convert rows to list of dictionaries
    columns = ["id", "position", "title", "link", "domain", "description", 
               "description_length", "result_type", "rating", "is_ad", "scraped_at"]
    data = []
    for row in rows:
        data.append(dict(zip(columns, row)))
    
    # Export to JSON
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"[SUCCESS] Exported {len(data)} results to: {filepath}")

# Clear the database
db.cursor.execute("DELETE FROM results")
db.conn.commit()
print("[SUCCESS] Database cleared.")

db.close()
