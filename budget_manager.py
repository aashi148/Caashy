import requests
import os

BUDGET = {
    "Food": 5000,
    "Transport": 2000,
    "Shopping": 3000,
    "Misc": 2000
}


def check_budget():
    from expense_tracker import pd, EXPENSE_FILE

    if not os.path.exists(EXPENSE_FILE):
        print("No data to analyze.")
        return

    df = pd.read_csv(EXPENSE_FILE)
    spent = df.groupby('Category')['Amount'].sum()

    print("\n Budget vs Spend:")
    for category, limit in BUDGET.items():
        used = spent.get(category, 0)
        print(f"{category}: Used ₹{used} / ₹{limit}")


def fetch_exchange_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/INR'
    res = requests.get(url).json()
    print("\n💱 INR Exchange Rates:")
    for c in ['USD', 'EUR', 'GBP', 'JPY']:
        print(f"{c}: {res['rates'][c]}")
