from db import schema, queries, seeds
import sqlite3

# List users function
def list_users():
    conn = sqlite3.connect('food_tracker.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, firstname, lastname FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

# Enter date
from datetime import datetime
def enter_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")

# Main
def main():

    # Create tables
    schema.create_tables()
    seeds.seed_data()

    # Welcome text
    print()
    print("Welcome to the Food Tracker!")
    print()

    # Select a user
    users = list_users()
    print("Select a user:")
    for user in users:
        print(f"{user[0]}: {user[1]} {user[2]}")
    user_id = int(input("\nEnter user ID: "))

    # User Options
    while True:
        print("""
        \nWhat would you like to do?
            1. Add food
            2. Update food amount
            3. Delete food
            4. List avaliable food to add
            5. View food entries
            6. View total calories
            7. Exit
        """)

        # User choice
        choice = input("Enter choice: ")

        # Add food
        if choice == "1":
            foods = queries.list_food()
            print("Select a food:")
            for food in foods:
                # print foods
                print(f"{food[0]}: {food[1]}")
            # get food id
            food_id = int(input("Enter food ID: "))
            # get amount
            amount = float(input("Enter number of ounces: "))
            # get date
            date = enter_date()
            # add food
            queries.add_food_entry(user_id, food_id, amount, date)
            print("Food entry added!")

        # Update food amount
        elif choice == "2":
            food_id = int(input("Enter food ID to update: "))
            new_amount = float(input("Enter new amount in ounces: "))
            date = enter_date()
            queries.update_food_amount(user_id, food_id, date, new_amount)
            print("Food amount updated!")

        # Delete food
        elif choice == "3":
            food_id = int(input("Enter food ID to delete: "))
            date = enter_date()
            queries.delete_food_entry(user_id, food_id, date)
            print("Food entry deleted!")

        # List avaliable food
        elif choice == "4":
            print("\nAvaliable foods:")
            total_foods = queries.list_food()
            for food in total_foods:
                print(f"{food[0]}: {food[1]} ({food[2]} Cal/oz)")

        # View food entries
        elif choice == "5":
            date = enter_date()
            print("\nFood entries:")
            food_entries = queries.get_food_entries(user_id, date)
            for entry in food_entries:
                print(f"{entry[0]} ounces of {entry[1]} on {entry[2]}")

        # View total calories
        elif choice == "6":
            date = enter_date()
            total = queries.get_total_calories(user_id, date)
            print(f"Total calories for {date}: {total} kcal")

        # Exit
        elif choice == "7":
            print("Thank you for using the Food Tracker!")
            break

        # Invalid choice
        else:
            print("Invalid choice. Please try again.")
            
# Run
if __name__ == "__main__":
    main()