from flask import Flask, render_template, request, redirect
from models import db, Transaction
from datetime import datetime
import os
from api_helpers import get_exchange_rates, get_crypto_price, get_financial_quote

app = Flask(__name__)

# ✅ Set up absolute path for data folder and database
basedir = os.path.abspath(os.path.dirname(__file__))
data_folder = os.path.join(basedir, 'data')
os.makedirs(data_folder, exist_ok=True)  # Ensure data folder exists

db_path = os.path.join(data_folder, 'expenses.db')

# ✅ Configuring the SQLite database with absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ✅ Initialize the database with the Flask app
db.init_app(app)

# ✅ Create tables if not exist
with app.app_context():
    db.create_all()

# ✅ Home route
@app.route('/')
def index():
    return render_template("index.html")

# ✅ Add expense route
@app.route('/add', methods=['POST'])
def add():
    amount = float(request.form['amount'])
    category = request.form['category']
    note = request.form.get('note', '')
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = Transaction(amount=amount, category=category, note=note, date=date)
    db.session.add(expense)
    db.session.commit()

    return redirect('/')

# ✅ API info route
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

if __name__ == '__main__':
    app.run(debug=True)
