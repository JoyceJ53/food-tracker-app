from .connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Insert users
    cursor.execute("INSERT OR IGNORE INTO users (id, firstname, lastname, age, gender, daily_calories) VALUES (1, 'Alice', 'Johnson', 30, 'Female', 2000)")
    cursor.execute("INSERT OR IGNORE INTO users (id, firstname, lastname, age, gender, daily_calories) VALUES (2, 'Bob', 'Smith', 25, 'Male', 2500)")

    # 2. Insert foods
    foods = [
        ("Apple", 14.0),
        ("Banana", 25.0),
        ("Chicken Breast", 47.0),
        ("Broccoli", 10.0),
        ("Rice", 37.0),
        ("Salmon", 58.0),
        ("Peanut Butter", 94.0),
        ("Egg", 44.0),
        ("Avocado", 45.0),
        ("Beef", 75.0)
    ]

    for i, (name, calories) in enumerate(foods, start=1):
        cursor.execute("INSERT OR IGNORE INTO food (id, food_name, calories_per_ounce) VALUES (?, ?, ?)", (i, name, calories))

    # 3. Insert food entries for each user
    food_logs = [
        (1, 1, 4.0, "2025-06-18"),  # Alice ate 4 oz Apple
        (1, 3, 6.0, "2025-06-18"),  # Alice ate Chicken Breast
        (1, 5, 3.0, "2025-06-18"),  # Alice ate Rice

        (2, 2, 2.0, "2025-06-18"),  # Bob ate Banana
        (2, 6, 5.0, "2025-06-18"),  # Bob ate Salmon
        (2, 8, 1.5, "2025-06-18")   # Bob ate Egg
    ]

    for entry in food_logs:
        cursor.execute("""
            INSERT OR REPLACE INTO user_food (user_id, food_id, amount, date)
            VALUES (?, ?, ?, ?)
        """, entry)

    conn.commit()
    conn.close()
