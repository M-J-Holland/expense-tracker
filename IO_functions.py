import json


def read_expenses():
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
        return expenses


def write_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
