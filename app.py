from flask import Flask, render_template, request, redirect, flash
from banking import Bank

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

if __name__ == '__main__':
    app.run(debug=True)
