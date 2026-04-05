import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv('/workspaces/Solo-Leveled/.env')

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "James_Bond"),
        database=os.getenv("DB_NAME", "")
    )

def test_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        print(f"Connected to: {cursor.fetchone()[0]}")
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    test_connection()
