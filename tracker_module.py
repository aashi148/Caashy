import pandas as pd
from datetime import datetime
import os
from models import db, Transaction
from flask import Flask

EXPENSE_FILE = 'data/expenses.csv'

# Needed to allow db access from script
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
data_folder = os.path.join(basedir, 'data')
db_path = os.path.join(data_folder, 'expenses.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def log_expense(amount, category, note=""):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = pd.DataFrame([[date, amount, category, note]],
                        columns=['Date', 'Amount', 'Category', 'Note'])

    # Save to CSV
    if not os.path.exists(EXPENSE_FILE):
        data.to_csv(EXPENSE_FILE, index=False)
    else:
        data.to_csv(EXPENSE_FILE, mode='a', header=False, index=False)

    # Save to database
    with app.app_context():
        transaction = Transaction(date=date, category=category, amount=amount, type="expense")
        db.session.add(transaction)
        db.session.commit()

    print(f"✅ Logged: ₹{amount} on {category}")

def view_expenses():
    if os.path.exists(EXPENSE_FILE):
        df = pd.read_csv(EXPENSE_FILE)
        print(df)
    else:
        print("No expenses logged yet.")


