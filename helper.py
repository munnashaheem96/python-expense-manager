
from datetime import datetime

expense = []


def menu():
    print("\n==========================")
    print("1 => Add Expense")
    print("2 => Display Expenses")
    print("3 => Delete Expense")
    print("4 => Update Expense")
    print("5 => Add Income")
    print("6 => View Balance")
    print("==========================")

    try:
        return int(input("Option Value: "))
    except ValueError:
        return 0


def get_date():
    while True:
        date = input("Enter Date (DD-MM-YYYY): ")

        try:
            valid_date = datetime.strptime(date, "%d-%m-%Y")
            return valid_date.strftime("%d-%m-%Y")
        except ValueError:
            print("Invalid Date! Please try again.")


def add_expense():
    typeofExpense = input("Type of Expense: ")

    print("1: UPI | 2: Cash")

    try:
        paymentModeNo = int(input("Select Option 1 or 2: "))

        if paymentModeNo == 1:
            paymentMode = "UPI"
        elif paymentModeNo == 2:
            paymentMode = "CASH"
        else:
            print("Invalid Option")
            return

        amount = int(input("Amount: "))

        if amount <= 0:
            print("Amount must be greater than zero")
            return

        date = get_date()

        expense.append((typeofExpense, paymentMode, amount, date))
        print("Expense Added Successfully!")

    except ValueError:
        print("Invalid Input")


def add_income():
    incomeType = input("Type of Income: ")

    try:
        amount = int(input("Amount: "))

        if amount <= 0:
            print("Amount must be greater than zero")
            return

        date = get_date()

        expense.append((incomeType, "INCOME", amount, date))
        print("Income Added Successfully!")

    except ValueError:
        print("Invalid Amount")


def display_expense():
    if not expense:
        print("No transactions available.")
        return

    print("\n========== TRANSACTIONS ==========")

    for i, item in enumerate(expense):
        print(f"{i}. {item[0]} | {item[1]} | Rs.{item[2]} | {item[3]}")

    print("=================================")


def delete_expense():
    display_expense()

    if not expense:
        return

    try:
        i = int(input("Enter the index you want to delete: "))

        if 0 <= i < len(expense):
            deleted = expense.pop(i)
            print("Deleted:", deleted)
        else:
            print("Invalid Index")

    except ValueError:
        print("Invalid Input")


def update_expense():
    display_expense()

    if not expense:
        return

    try:
        i = int(input("Enter the index you want to update: "))

        if not (0 <= i < len(expense)):
            print("Invalid Index")
            return

        old_item = expense[i]

        typeofExpense = input("Type: ")

        if old_item[1] == "INCOME":
            paymentMode = "INCOME"
        else:
            print("1: UPI | 2: Cash")
            paymentModeNo = int(input("Select Option 1 or 2: "))

            if paymentModeNo == 1:
                paymentMode = "UPI"
            elif paymentModeNo == 2:
                paymentMode = "CASH"
            else:
                print("Invalid Option")
                return

        amount = int(input("Amount: "))

        if amount <= 0:
            print("Amount must be greater than zero")
            return

        date = get_date()

        expense[i] = (typeofExpense, paymentMode, amount, date)

        print("Updated Successfully!")

    except ValueError:
        print("Invalid Input")


def view_balance():
    total_income = 0
    total_expense = 0

    for item in expense:
        if item[1] == "INCOME":
            total_income += item[2]
        else:
            total_expense += item[2]

    balance = total_income - total_expense

    print("\n========== ACCOUNT SUMMARY ==========")
    print(f"Total Income   : Rs.{total_income}")
    print(f"Total Expense  : Rs.{total_expense}")
    print("-------------------------------------")
    print(f"Current Balance: Rs.{balance}")
    print("=====================================")


def get_expense():
    return expense


def set_expense(d):
    global expense
    expense = [] if d is None else d
