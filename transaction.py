import numpy as np

class transaction:
    id = 0
    
    def __init__(self):
        self.ID = transaction.id
        x = np.random.normal(5, 10)
        while x <= 0:
            x = np.random.normal(5, 10)
        self.BTC = "Sent " + str(x) + " BTC"
        y = np.random.normal(x/10, 1)
        while y <= 0 or y > x/10:
            y = np.random.normal(x/100, 0.1)
        self.Fee = y
        transaction.id += 1


    def new_transaction():
        nt = transaction()
        return {'ID': nt.ID, 'Data': nt.BTC, 'Fee' : nt.Fee}
