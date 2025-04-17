# create_db.py
import os
from flask import Flask
from models import db, Transaction

app = Flask(__name__)

# Define absolute path to the database
basedir = os.path.abspath(os.path.dirname(__file__))
db_folder = os.path.join(basedir, 'data')
db_path = os.path.join(db_folder, 'budget.db')

# Create data folder if it doesn't exist
os.makedirs(db_folder, exist_ok=True)

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

# Create the tables and insert sample data
with app.app_context():
    db.drop_all()
    db.create_all()

    sample_data = [
        Transaction(date="2025-04-01", category="Salary", amount=3000, type="income"),
        Transaction(date="2025-04-03", category="Groceries", amount=150, type="expense"),
        Transaction(date="2025-04-05", category="Electricity", amount=90, type="expense"),
        Transaction(date="2025-04-06", category="Investment", amount=500, type="income"),
    ]

    db.session.add_all(sample_data)
    db.session.commit()
    print("✅ Database created and sample data inserted.")
