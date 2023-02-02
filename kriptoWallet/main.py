# u bazu ide koja valuta, koliko je imamo i koji datum


import tkinter as tk

from gui import AccountBalance, BalanceList

if __name__=="__main__":
    root = tk.Tk()
    root.geometry("300x300")
    root.title("KriptoWallet")

    gui_balance = AccountBalance(root)

    balance_list = BalanceList(root)

    root.mainloop()