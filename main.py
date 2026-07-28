from expense_functions import add_expenses, show_expenses, show_expense_total, menu


# main while loop
def main():
    print("Welcome to the CLI expense tracker.")
    menu()
    while True:
        # user_choice while loop
        while True:
            user_choice = input("\nChoice: ")
            try:
                user_choice = int(user_choice)
                break
            except ValueError:
                print("Please only enter a number")
        if user_choice == 1:
            add_expenses()
            menu()
        elif user_choice == 2:
            shown_expenses = show_expenses()
            print(shown_expenses)
            menu()
        elif user_choice == 3:
            expense_total = show_expense_total()
            print(expense_total)
            menu()
        elif user_choice == 4:
            print("Goodbye.")
            break
        else:
            print("You appear to have inputted an option that doesn't seem to exist, please try again\n")
            for index, choice in enumerate(options, start=1):
                print(f"{index} - {choice}")


if __name__ == '__main__':
    main()
