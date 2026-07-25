print("Welcome to the CLI expense tracker.")

options = ["Add Expense", "View Expense", "Show Total", "Exit"]

for index, choice in enumerate(options, start=1):
    print(f"{index} - {choice}")

user_choice = int(input("\nChoice: "))