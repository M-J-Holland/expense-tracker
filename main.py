import json

print("Welcome to the CLI expense tracker.")

options = ["Add Expense", "View Expenses", "Show Total", "Exit"]

for index, choice in enumerate(options, start=1):
    print(f"{index} - {choice}")
# main while loop
while True:
    # user_choice while loop
    while True:
        user_choice = input("\nChoice: ")

        try:
            user_choice = int(user_choice)
            break
        except ValueError:
            print("Please only enter a number")

    if user_choice == 1: # Add Expense
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

    elif user_choice == 2: # Show Expenses
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
        if not expenses:
            print("You currently have no expenses to show. After you've added some, come back here to see them.")
            continue
        for expense in expenses:
            print(f"{expense['description']}, {expense['amount']:.2f}, {expense['category']}")

    elif user_choice == 3: # Show Expense total
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
        if not expenses:
            print("You currently have no expenses to show the total. After you've added some, come back here to see "
                  "them.")
            continue
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print(f"Your total expenses are: £{total:.2f}")
    elif user_choice == 4:
        print("Goodbye.")
        break
    else:
        print("You appear to have inputted an option that doesn't seem to exist, please try again\n")
        for index, choice in enumerate(options, start=1):
            print(f"{index} - {choice}")
