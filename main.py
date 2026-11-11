
import tkinter as tk
from tkinter import ttk, messagebox

from helper import *
from fileop import *


# Load previous data
set_expense(read_data_from_file())


# Main Window
root = tk.Tk()

root.title("Expense Tracker")
root.geometry("1100x720")
root.minsize(900, 600)

root.configure(bg="#f1f5f9")


# Colors
BG = "#f1f5f9"
WHITE = "#ffffff"
BLUE = "#2563eb"
GREEN = "#16a34a"
RED = "#dc2626"
DARK = "#1e293b"
GRAY = "#64748b"


# Style
style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Treeview",
    background=WHITE,
    foreground=DARK,
    rowheight=32,
    fieldbackground=WHITE,
    font=("Arial", 10)
)

style.configure(
    "Treeview.Heading",
    background="#e2e8f0",
    foreground=DARK,
    font=("Arial", 10, "bold")
)


# Save Data
def save_data():
    write_to_file(get_expense())


# Update Balance
def update_balance():

    income, expenses, balance = view_balance()

    income_label.config(text=f"₹ {income}")
    expense_label.config(text=f"₹ {expenses}")
    balance_label.config(text=f"₹ {balance}")


# Refresh Table
def refresh_table():

    for row in table.get_children():
        table.delete(row)

    for i, item in enumerate(get_expense()):

        table.insert(
            "",
            "end",
            iid=str(i),
            values=(
                item[0],
                item[1],
                f"₹ {item[2]}",
                item[3]
            )
        )

    update_balance()


# Clear Form
def clear_fields():

    type_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

    payment_box.set("UPI")

    table.selection_remove(table.selection())


# Add Transaction
def add_transaction():

    typeofExpense = type_entry.get().strip()
    paymentMode = payment_box.get()
    amount = amount_entry.get().strip()
    date = date_entry.get().strip()

    if not typeofExpense or not amount or not date:

        messagebox.showerror(
            "Error",
            "Please fill all fields"
        )

        return

    if paymentMode not in ["UPI", "CASH", "INCOME"]:

        messagebox.showerror(
            "Error",
            "Select a valid payment mode"
        )

        return

    try:
        amount = int(amount)

        if amount <= 0:
            raise ValueError

    except ValueError:

        messagebox.showerror(
            "Error",
            "Enter a valid positive amount"
        )

        return

    if not validate_date(date):

        messagebox.showerror(
            "Invalid Date",
            "Enter date in DD-MM-YYYY format"
        )

        return

    if paymentMode == "INCOME":

        add_income(
            typeofExpense,
            amount,
            date
        )

    else:

        add_expense(
            typeofExpense,
            paymentMode,
            amount,
            date
        )

    save_data()
    refresh_table()
    clear_fields()

    messagebox.showinfo(
        "Success",
        "Transaction added successfully!"
    )


# Select Transaction
def select_transaction(event):

    selected = table.selection()

    if not selected:
        return

    index = int(selected[0])

    item = get_expense()[index]

    type_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

    type_entry.insert(0, item[0])
    payment_box.set(item[1])
    amount_entry.insert(0, str(item[2]))
    date_entry.insert(0, item[3])


# Update Transaction
def update_transaction():

    selected = table.selection()

    if not selected:

        messagebox.showwarning(
            "Warning",
            "Select a transaction to update"
        )

        return

    index = int(selected[0])

    typeofExpense = type_entry.get().strip()
    paymentMode = payment_box.get()
    amount = amount_entry.get().strip()
    date = date_entry.get().strip()

    if not typeofExpense or not amount or not date:

        messagebox.showerror(
            "Error",
            "Please fill all fields"
        )

        return

    if paymentMode not in ["UPI", "CASH", "INCOME"]:

        messagebox.showerror(
            "Error",
            "Select a valid payment mode"
        )

        return

    try:

        amount = int(amount)

        if amount <= 0:
            raise ValueError

    except ValueError:

        messagebox.showerror(
            "Error",
            "Invalid amount"
        )

        return

    if not validate_date(date):

        messagebox.showerror(
            "Error",
            "Invalid date format"
        )

        return

    update_expense(
        index,
        typeofExpense,
        paymentMode,
        amount,
        date
    )

    save_data()
    refresh_table()
    clear_fields()

    messagebox.showinfo(
        "Success",
        "Transaction updated successfully!"
    )


# Delete Transaction
def delete_transaction():

    selected = table.selection()

    if not selected:

        messagebox.showwarning(
            "Warning",
            "Select a transaction to delete"
        )

        return

    index = int(selected[0])

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this transaction?"
    )

    if confirm:

        delete_expense(index)

        save_data()
        refresh_table()
        clear_fields()

        messagebox.showinfo(
            "Success",
            "Transaction deleted successfully!"
        )


# Header
header = tk.Frame(
    root,
    bg=DARK,
    height=80
)

header.pack(fill="x")

tk.Label(
    header,
    text="EXPENSE TRACKER",
    font=("Arial", 22, "bold"),
    bg=DARK,
    fg=WHITE
).pack(pady=20)


# Dashboard
dashboard = tk.Frame(
    root,
    bg=BG
)

dashboard.pack(
    fill="x",
    padx=25,
    pady=20
)


# Dashboard Card
def create_card(parent, title, color):

    card = tk.Frame(
        parent,
        bg=WHITE,
        padx=20,
        pady=15,
        highlightbackground="#e2e8f0",
        highlightthickness=1
    )

    tk.Label(
        card,
        text=title,
        font=("Arial", 11),
        bg=WHITE,
        fg=GRAY
    ).pack(anchor="w")

    value = tk.Label(
        card,
        text="₹ 0",
        font=("Arial", 20, "bold"),
        bg=WHITE,
        fg=color
    )

    value.pack(anchor="w", pady=8)

    return card, value


card1, income_label = create_card(
    dashboard,
    "TOTAL INCOME",
    GREEN
)

card2, expense_label = create_card(
    dashboard,
    "TOTAL EXPENSE",
    RED
)

card3, balance_label = create_card(
    dashboard,
    "CURRENT BALANCE",
    BLUE
)

card1.pack(
    side="left",
    expand=True,
    fill="x",
    padx=5
)

card2.pack(
    side="left",
    expand=True,
    fill="x",
    padx=5
)

card3.pack(
    side="left",
    expand=True,
    fill="x",
    padx=5
)


# Main Content
content = tk.Frame(
    root,
    bg=BG
)

content.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=5
)


# Transaction Form
form = tk.LabelFrame(
    content,
    text="Transaction Details",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=DARK,
    padx=15,
    pady=15
)

form.pack(
    side="left",
    fill="y",
    padx=(0, 15)
)


# Type
tk.Label(
    form,
    text="Transaction Type",
    bg=WHITE,
    fg=DARK
).pack(anchor="w", pady=(5, 3))

type_entry = ttk.Entry(
    form,
    width=27
)

type_entry.pack(pady=5)


# Payment Mode
tk.Label(
    form,
    text="Payment Mode",
    bg=WHITE,
    fg=DARK
).pack(anchor="w", pady=(10, 3))

payment_box = ttk.Combobox(
    form,
    values=["UPI", "CASH", "INCOME"],
    state="readonly",
    width=24
)

payment_box.set("UPI")
payment_box.pack(pady=5)


# Amount
tk.Label(
    form,
    text="Amount (₹)",
    bg=WHITE,
    fg=DARK
).pack(anchor="w", pady=(10, 3))

amount_entry = ttk.Entry(
    form,
    width=27
)

amount_entry.pack(pady=5)


# Date
tk.Label(
    form,
    text="Date (DD-MM-YYYY)",
    bg=WHITE,
    fg=DARK
).pack(anchor="w", pady=(10, 3))

date_entry = ttk.Entry(
    form,
    width=27
)

date_entry.pack(pady=5)


# Add Button
tk.Button(
    form,
    text="Add Transaction",
    bg=BLUE,
    fg=WHITE,
    width=24,
    relief="flat",
    command=add_transaction
).pack(pady=(20, 7))


# Update Button
tk.Button(
    form,
    text="Update Transaction",
    bg=GREEN,
    fg=WHITE,
    width=24,
    relief="flat",
    command=update_transaction
).pack(pady=7)


# Delete Button
tk.Button(
    form,
    text="Delete Transaction",
    bg=RED,
    fg=WHITE,
    width=24,
    relief="flat",
    command=delete_transaction
).pack(pady=7)


# Clear Button
tk.Button(
    form,
    text="Clear Fields",
    bg="#64748b",
    fg=WHITE,
    width=24,
    relief="flat",
    command=clear_fields
).pack(pady=7)


# Transaction Table
table_frame = tk.LabelFrame(
    content,
    text="All Transactions",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=DARK,
    padx=10,
    pady=10
)

table_frame.pack(
    side="left",
    fill="both",
    expand=True
)


columns = (
    "type",
    "mode",
    "amount",
    "date"
)


table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    selectmode="browse"
)


table.heading("type", text="Type")
table.heading("mode", text="Mode")
table.heading("amount", text="Amount")
table.heading("date", text="Date")


table.column("type", width=130)
table.column("mode", width=80)
table.column("amount", width=110)
table.column("date", width=110)


# Scrollbar
scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=table.yview
)

table.configure(
    yscrollcommand=scrollbar.set
)


table.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# Table Selection Event
table.bind(
    "<<TreeviewSelect>>",
    select_transaction
)


# Initial Data
refresh_table()


# Footer
footer = tk.Label(
    root,
    text="Expense Tracker | Python + Tkinter",
    bg=BG,
    fg=GRAY,
    font=("Arial", 9)
)

footer.pack(pady=10)


# Run Application
root.mainloop()
