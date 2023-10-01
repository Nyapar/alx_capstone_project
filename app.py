from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample initial balance
current_balance = 1000

# Sample list of transactions
transactions = []

@app.route('/')
def index():
    return render_template('index.html', current_balance=current_balance, transactions=transactions)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    global current_balance
    description = request.form.get('description')
    category = request.form.get('category')
    amount = float(request.form.get('amount'))

    # Update the current balance
    current_balance += amount

    # Add the transaction to the list
    transactions.append({
        'description': description,
        'category': category,
        'amount': amount
    })

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

