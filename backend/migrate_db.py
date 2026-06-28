import sqlite3
from datetime import datetime
import os

db_path = os.path.join(os.path.dirname(__file__), 'instance', 'hms.db')

def migrate():
    print(f"Opening database: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Add contact column to doctors table
    try:
        cursor.execute("ALTER TABLE doctors ADD COLUMN contact VARCHAR(15)")
        print("Added 'contact' column to 'doctors' table.")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e).lower():
            print("'contact' column already exists in 'doctors' table.")
        else:
            print(f"Error adding 'contact' column to 'doctors': {e}")
            
    # 2. Add registration_date column to patients table
    try:
        cursor.execute("ALTER TABLE patients ADD COLUMN registration_date VARCHAR(10)")
        print("Added 'registration_date' column to 'patients' table.")
        
        # Populate registration_date for existing patients
        today = datetime.now().strftime('%Y-%m-%d')
        cursor.execute("UPDATE patients SET registration_date = ? WHERE registration_date IS NULL", (today,))
        print(f"Populated NULL 'registration_date' values with default: {today}")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e).lower():
            print("'registration_date' column already exists in 'patients' table.")
        else:
            print(f"Error adding 'registration_date' column to 'patients': {e}")
            
    conn.commit()
    conn.close()
    print("Database migration completed.")

if __name__ == '__main__':
    migrate()
