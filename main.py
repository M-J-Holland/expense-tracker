import json

print("Welcome to the CLI expense tracker.")

options = ["Add Expense", "View Expense", "Show Total", "Exit"]

for index, choice in enumerate(options, start=1):
    print(f"{index} - {choice}")
while True:
    while True:
        user_choice = input("\nChoice: ")

        try:
            user_choice = int(user_choice)
            break
        except ValueError:
            print("Please only enter a number")

    if user_choice == 1:
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

    elif user_choice == 2:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
        for  expense in expenses:
            print(f"{expense["description"]}, {expense["amount"]}, {expense["category"]}")