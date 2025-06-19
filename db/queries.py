from .connection import get_connection

# add food entry
def add_food_entry(user_id, food_id, amount, date):
    # connect to db
    conn = get_connection()
    cursor = conn.cursor()

    # SQL add food entry query
    cursor.execute("""
        INSERT OR REPLACE INTO user_food (user_id, food_id, amount, date)
        VALUES (?, ?, ?, ?)
    """, (user_id, food_id, amount, date))

    # commit and close connection
    conn.commit()
    conn.close()

# delete food entry
def delete_food_entry(user_id, food_id, date):
    # connect to db
    conn = get_connection()
    cursor = conn.cursor()

    # SQL delete food entry query
    cursor.execute("""
        DELETE FROM user_food
        WHERE user_id = ? AND food_id = ? AND date = ?
    """, (user_id, food_id, date))

    # commit and close connection
    conn.commit()
    conn.close()

# update food amount
def update_food_amount(user_id, food_id, date, new_amount):
    # connect to db
    conn = get_connection()
    cursor = conn.cursor()

    # SQL update food amount query
    cursor.execute("""
        UPDATE user_food
        SET amount = ?
        WHERE user_id = ? AND food_id = ? AND date = ?
    """, (new_amount, user_id, food_id, date))

    # commit and close connection
    conn.commit()
    conn.close()

# list food
def list_food():
    # connect to db
    conn = get_connection()
    cursor = conn.cursor()

    # SQL list food query
    cursor.execute("SELECT id, food_name, calories_per_ounce FROM food")

    # fetch all rows
    foods = cursor.fetchall()

    # close connection
    conn.close()

    # return foods
    return foods

# get food entries
def get_food_entries(user_id,date):
    # connect to db
    conn = get_connection()
    cursor = conn.cursor()

    # SQL get food entries query
    cursor.execute("""
        SELECT uf.amount, f.food_name, uf.date FROM user_food uf
        JOIN food f ON uf.food_id = f.id
        WHERE uf.user_id = ? AND uf.date = ?
    """, (user_id, date))

    # fetch all rows
    entries = cursor.fetchall()

    # close connection
    conn.close()

    # return entries
    return entries

# get total calories
def get_total_calories(user_id, date):
    # connect to db
    conn = get_connection()
    cursor = conn.cursor()

    # SQL get total calories query
    cursor.execute("""
        SELECT SUM(f.calories_per_ounce * uf.amount) AS total_calories
        FROM user_food uf
        JOIN food f ON uf.food_id = f.id
        WHERE uf.user_id = ? AND uf.date = ?
    """, (user_id, date))
    total = cursor.fetchone()[0]

    # commit and close connection
    conn.close()

    # return total calories
    return total or 0