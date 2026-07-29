from IO_functions import read_expenses, write_expenses
import time


def menu():
    options = ["Add Expense", "View Expenses", "Show Total", "Exit"]
    print()
    for index, choice in enumerate(options, start=1):
        print(f"{index} - {choice}")


def check_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value


def check_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("Please only enter a number e.g. 4, 3.14")


def add_expenses():
    expenses = read_expenses()

    description = check_input("Description: ")
    amount = check_amount("Amount: ")
    category = check_input("Category: ")

    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    write_expenses(expenses)
    print("Adding your expenses now...")
    time.sleep(1)
    print("Expenses successfully added.")


def show_expenses():  # Show Expenses
    expenses = read_expenses()
    if not expenses:
        return "You currently have no expenses to show. After you've added some, come back here to see them."

    expense_list = []
    for expense in expenses:
        expense_list.append(f"{expense['description']}, £{expense['amount']:.2f}, {expense['category']}")
    return "\n".join(expense_list)


def show_expense_total():  # Show Expense total
    expenses = read_expenses()
    if not expenses:
        return "You currently have no expenses to show the total. After you've added some, come back here to see them."

    total = 0
    for expense in expenses:
        total += expense["amount"]
    return f"Your total expenses are: £{total:.2f}"
