from flask import Flask, render_template, request, redirect
from models import db, Expense
from datetime import datetime
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db.init_app(app)

with app.app_context():
    os.makedirs('', exist_ok=True)
    db.create_all()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/add', methods=['POST'])
def add():
    amount = float(request.form['amount'])
    category = request.form['category']
    note = request.form.get('note', '')
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = Expense(amount=amount, category=category, note=note, date=date)
    db.session.add(expense)
    db.session.commit()

    return redirect('/')


from api_helpers import get_exchange_rates, get_crypto_price, get_financial_quote


@app.route('/api-info')
def api_info():
    fx = get_exchange_rates('INR')
    btc = get_crypto_price('bitcoin')
    quote = get_financial_quote()

    return {
        "ExchangeRateUSDINR": fx['rates']['INR'],
        "BitcoinPriceUSD": btc,
        "FinanceQuote": quote
    }
