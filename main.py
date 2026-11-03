
import csv
import os

FILE_NAME = "expenses.csv"


# Function to save an expense
def save_expense(expense):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([expense["name"], expense["amount"]])


# Function to load previous expenses
def load_expenses():
    expenses = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 2:
                    expense = {
                        "name": row[0],
                        "amount": float(row[1])
                    }
                    expenses.append(expense)

    return expenses


# Main program
print("================================")
print("  PERSONAL EXPENSE TRACKER")
print("================================")

name = input("Enter your name: ")

# Load previously saved expenses
expenses = load_expenses()

print("\nHello", name)
print("Welcome back to your Expense Tracker!")


# Main menu
while True:

    print("\n----- EXPENSE TRACKER MENU -----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add expense
    if choice == "1":

        expense_name = input("Enter expense name: ")

        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Please enter an amount greater than zero.")
                continue

        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue

        expense = {
            "name": expense_name,
            "amount": amount
        }

        expenses.append(expense)
        save_expense(expense)

        print("Expense added successfully!")

    # View expenses
    elif choice == "2":

        print("\n----- YOUR EXPENSES -----")

        if len(expenses) == 0:
            print("No expenses added yet.")

        else:
            for i, expense in enumerate(expenses, start=1):
                print(
                    i, ".",
                    expense["name"],
                    "- Rs.", expense["amount"]
                )

    # Calculate total
    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("\nTotal Expenses: Rs.", total)

    # Exit
    elif choice == "4":

        print("\nThank you for using Personal Expense Tracker!")
        print("Goodbye", name)
        break

    # Invalid choice
    else:
        print("Invalid choice! Please select 1, 2, 3 or 4.")
