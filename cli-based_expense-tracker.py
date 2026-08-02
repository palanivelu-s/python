import os
import csv

FILE_NAME = "expenses.txt"


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")

    while True:
        try:
            amount = float(input("Enter amount: ₹"))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!\n")


def view_expenses():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No expenses found.\n")
        return

    print("\n========== Expense List ==========")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)

        for i, row in enumerate(reader, start=1):
            date, category, amount, description = row

            print(f"{i}. Date        : {date}")
            print(f"   Category    : {category}")
            print(f"   Amount      : ₹{float(amount):.2f}")
            print(f"   Description : {description}")
            print("-" * 35)


def total_expense():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No expenses found.\n")
        return

    total = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            total += float(row[2])

    print(f"\nTotal Expense: ₹{total:.2f}\n")


def delete_expense():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No expenses found.\n")
        return

    expenses = []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        expenses = list(reader)

    print("\nExpenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense[0]} | {expense[1]} | ₹{expense[2]} | {expense[3]}")

    try:
        choice = int(input("\nEnter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            deleted = expenses.pop(choice - 1)

            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(expenses)

            print(f"Deleted expense: {deleted[1]} - ₹{deleted[2]}\n")
        else:
            print("Invalid expense number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def reset_expenses():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No expenses found.\n")
        return

    confirm = input("Are you sure you want to delete ALL expenses? (yes/no): ").lower()

    if confirm == "yes":
        open(FILE_NAME, "w").close()
        print("All expenses deleted successfully!\n")
    else:
        print("Reset cancelled.\n")


def menu():
    while True:
        print("========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expense")
        print("4. Delete Expense")
        print("5. Reset All Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            reset_expenses()
        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    menu()
