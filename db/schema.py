from .connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Create User Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT NOT NULL,
        daily_calories INTEGER
    )
    """)

    # Create Food Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS food (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        food_name TEXT NOT NULL,
        calories_per_ounce REAL NOT NULL
    )
    """)

    # Create User Food Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_food (
        user_id INTEGER,
        food_id INTEGER,
        amount REAL NOT NULL,   -- in ounces
        date TEXT NOT NULL,     -- format:  YYYY-MM-DD
        PRIMARY KEY (user_id, food_id, date),
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (food_id) REFERENCES food(id)
    )
    """)

    conn.commit()
    conn.close()