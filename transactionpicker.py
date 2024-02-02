
import threading
import time
from flask import Flask, jsonify
from data import transactions_list
from transaction import transaction



# Create Web App
app = Flask(__name__)


for i in range(0, 100):
    transactions_list.append(transaction.new_transaction())

def add_transactions_periodically():
    while True:
        time.sleep(30) 
        for i in range(15):
            transactions_list.append(transaction.new_transaction())
        print(f"Added 15 new transactions to the list.: {transactions_list[len(transactions_list)-5:len(transactions_list)]}")

thread = threading.Thread(target=add_transactions_periodically)
thread.daemon = True  
thread.start()

# returns list of transactions
@app.route('/get_transactions', methods=['GET'])
def get_transactions():
    response = {'Transactions': transactions_list}
    return jsonify(response), 200


def sort_transactions(transactions):
    x = transactions.copy()
    n = len(x)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if x[j]['Fee'] > x[j + 1]['Fee']:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


# Returns list of 10 transactions with highest fees
@app.route('/get_ten_highest_fees', methods=['GET'])
def get_ten_highest_Fees():
    sortedlist = sort_transactions(transactions_list)
    response = {'Transactions': sortedlist[len(sortedlist)-10:len(sortedlist)]}
    return jsonify(response), 200




# Returns list of 10 transactions with lowest fees
@app.route('/get_ten_lowest_fees', methods=['GET'])
def get_ten_lowest_fees():
    sortedlist = sort_transactions(transactions_list)
    response = {'Transactions': sortedlist[0:10]} # placeholder
    return jsonify(response), 200


    


# Returns second highest total fee sum after picking 10 transactions
@app.route('/get_next_highest_total', methods=['GET'])
def get_next_highest_total():
    sortedlist = sort_transactions(transactions_list)
    x = 0
    
    for i in sortedlist[len(transactions_list)-9:len(transactions_list)]:
        x += i['Fee']
    x += sortedlist[len(transactions_list)-11]['Fee']
    response = {'Total Fee': x} # placeholder
    return jsonify(response), 200
    



# Run app
app.run(host='0.0.0.0', port=5050)
