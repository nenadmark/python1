import tkinter as tk
from api import get_Crypto_values

currencies = {
    'BTC': {
        'name': "BTC", 
        'amount': 0.7, 
        'price': 14.000
    },
    'ETH': {
        'name': "ETH", 
        'amount': 3, 
        'price': 14.000
    },
    'SOL': {
        'name': "SOL", 
        'amount': 10, 
        'price': 14.000
    }
}

class AccountBalance:
    def __init__(self, root):
        self.root = root
        self.frame = self.create_label_frame()
        self.balance = tk.StringVar(value="20.000.00€")

    def create_label_frame(self):
        label_frame = tk.LabelFrame(self.root, text="Account Balance")
        label_frame.grid(row=0, column=0, padx=10, pady=10)
        return label_frame

    def create_balance_label(self):
        balance_label = tk.Label(self.frame, textvariable=self.balance)
        balance_label.grid(row=0, column=0, padx=10, pady=10)
        return balance_label


class BalanceList:
    def __init__(self, root):
        self.root = root
        self.currency_frame = self.create_currency_frame()
        self.total_value = tk.StringVar(value="20.000.00€")

    def create_currency_frame(self):
        label_frame = tk.LabelFrame(self.root, text="Balance List")
        label_frame.grid(row=1, column=0, padx=10, pady=10)
        return label_frame

    def create_currency_labels(self):
        for idx, value in enumerate(currencies.values()):
            currency_label = tk.Label(self.currency_frame, text=value["name"])
            currency_label.grid(row=idx, column=0, padx=10, pady=10)
            percentage = (value["price"] / self.total_value) * 100
            value_label = tk.Label(self.currency_frame, text=f"{value['price']} € {percentage}%")
            value_label.grid(row=idx, column=1, padx=10, pady=10)
