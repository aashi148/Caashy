import pandas as pd
from datetime import datetime
import os

EXPENSE_FILE = 'data/expenses.csv'


def log_expense(amount, category, note=""):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = pd.DataFrame([[date, amount, category, note]],
                        columns=['Date', 'Amount', 'Category', 'Note'])

    if not os.path.exists(EXPENSE_FILE):
        data.to_csv(EXPENSE_FILE, index=False)
    else:
        data.to_csv(EXPENSE_FILE, mode='a', header=False, index=False)

    print(f"Logged: ₹{amount} on {category}")


def view_expenses():
    if os.path.exists(EXPENSE_FILE):
        df = pd.read_csv(EXPENSE_FILE)
        print(df)
    else:
        print("No expenses logged yet.")

def track_expenses():
    # TODO: Add real logic here
    print("Tracking expenses...")