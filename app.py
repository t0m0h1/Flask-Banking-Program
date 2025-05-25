from flask import Flask, render_template, request, redirect, flash
from banking import Bank
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flashing messages

bank = Bank()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    try:
        account_number = request.form['account_number']
        initial_balance = float(request.form.get('initial_balance', 0))
        bank.create_account(account_number, initial_balance)
        flash(f"Account {account_number} created successfully!", "success")
    except Exception as e:
        flash(str(e), "error")
    return redirect('/')

@app.route('/deposit', methods=['POST'])
def deposit():
    try:
        account_number = request.form['account_number']
        amount = float(request.form['amount'])
        bank.deposit(account_number, amount)
        flash(f"Deposited ${amount:.2f} to account {account_number}.", "success")
    except Exception as e:
        flash(str(e), "error")
    return redirect('/')

@app.route('/withdraw', methods=['POST'])
def withdraw():
    try:
        account_number = request.form['account_number']
        amount = float(request.form['amount'])
        bank.withdraw(account_number, amount)
        flash(f"Withdrew ${amount:.2f} from account {account_number}.", "success")
    except Exception as e:
        flash(str(e), "error")
    return redirect('/')

@app.route('/transfer', methods=['POST'])
def transfer():
    try:
        from_account = request.form['from_account']
        to_account = request.form['to_account']
        amount = float(request.form['amount'])
        bank.transfer(from_account, to_account, amount)
        flash(f"Transferred ${amount:.2f} from {from_account} to {to_account}.", "success")
    except Exception as e:
        flash(str(e), "error")
    return redirect('/')

@app.route('/get_balance', methods=['POST'])
def get_balance():
    try:
        account_number = request.form['account_number']
        balance = bank.get_balance(account_number)
        flash(f"Account {account_number} has a balance of ${balance:.2f}.", "info")
    except Exception as e:
        flash(str(e), "error")
    return redirect('/')

@app.route('/get_all_accounts', methods=['GET'])
def get_all_accounts():
    try:
        accounts = bank.get_all_accounts()
        return render_template('accounts.html', accounts=accounts)
    except Exception as e:
        flash(str(e), "error")
        return redirect('/')
    

@app.route('/delete_account', methods=['POST'])
def delete_account():
    try:
        account_number = request.form['account_number']
        bank.delete_account(account_number)
        flash(f"Account {account_number} deleted successfully!", "success")
    except Exception as e:
        flash(str(e), "error")
    return redirect('/')




# Routes for sign up and login
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you would typically save the user to a database
        flash(f"User {username} signed up successfully!", "success")
        return redirect('/')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you would typically check the user credentials against a database
        flash(f"User {username} logged in successfully!", "success")
        return redirect('/')
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')
    conn.commit()
