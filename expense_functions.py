import json


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


def show_expenses():  # Show Expenses
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
    if not expenses:
        return "You currently have no expenses to show. After you've added some, come back here to see them."
    else:
        for expense in expenses:
            return f"{expense['description']}, {expense['amount']:.2f}, {expense['category']}"


def show_expense_total():  # Show Expense total
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
    if not expenses:
        return "You currently have no expenses to show the total. After you've added some, come back here to see them."

    total = 0
    for expense in expenses:
        total += expense["amount"]
    return f"Your total expenses are: £{total:.2f}"
