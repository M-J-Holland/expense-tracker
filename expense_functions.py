import json
import time


def menu():
    options = ["Add Expense", "View Expenses", "Show Total", "Exit"]
    print()
    for index, choice in enumerate(options, start=1):
        print(f"{index} - {choice}")


def add_expenses():
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    description = input("Description: ")
    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Please only enter a number e.g 4, 3.14")

    category = input("Category: ")

    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }
    
    expenses.append(expense)

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
    print("Adding your expenses now...")
    time.sleep(1)
    print("Expenses successfully added.")


def show_expenses():  # Show Expenses
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
    if not expenses:
        return "You currently have no expenses to show. After you've added some, come back here to see them."

    expense_list = []
    for expense in expenses:
        expense_list.append(f"{expense['description']}, £{expense['amount']:.2f}, {expense['category']}")
    return "\n".join(expense_list)


def show_expense_total():  # Show Expense total
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
    if not expenses:
        return "You currently have no expenses to show the total. After you've added some, come back here to see them."

    total = 0
    for expense in expenses:
        total += expense["amount"]
    return f"Your total expenses are: £{total:.2f}"
