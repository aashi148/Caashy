from tracker_module import log_expense, view_expenses

from budget_manager import check_budget, fetch_exchange_rates
from utils import get_inflation, get_spending_tip

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Check Budget\n4. Exchange Rates\n5. Inflation\n6. Tip\n0. Exit")
    choice = input("Choose: ")

    if choice == "1":
        amt = float(input("Amount: ₹"))
        cat = input("Category: ")
        note = input("Note: ")
        log_expense(amt, cat, note)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        check_budget()
    elif choice == "4":
        fetch_exchange_rates()
    elif choice == "5":
        get_inflation()
    elif choice == "6":
        get_spending_tip()
    elif choice == "0":
        break
    else:
        print("Invalid choice.")