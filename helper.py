
from datetime import datetime

expense = []


def add_expense(typeofExpense, paymentMode, amount, date):
    expense.append((typeofExpense, paymentMode, amount, date))


def add_income(incomeType, amount, date):
    expense.append((incomeType, "INCOME", amount, date))


def display_expense():
    return expense


def delete_expense(index):
    if 0 <= index < len(expense):
        return expense.pop(index)

    return None


def update_expense(index, typeofExpense, paymentMode, amount, date):
    if 0 <= index < len(expense):
        expense[index] = (
            typeofExpense,
            paymentMode,
            amount,
            date
        )
        return True

    return False


def view_balance():
    total_income = 0
    total_expense = 0

    for item in expense:
        if item[1] == "INCOME":
            total_income += item[2]
        else:
            total_expense += item[2]

    balance = total_income - total_expense

    return total_income, total_expense, balance


def get_expense():
    return expense


def set_expense(data):
    global expense
    expense = [] if data is None else data


def validate_date(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True

    except ValueError:
        return False
