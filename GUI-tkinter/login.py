import tkinter as tk
from tkinter import DISABLED, ttk

root = tk.Tk()
root.title("Algebra / TKINTER LOGIN")
root.geometry("350x220")
# ako ne navedemo geometry, onda tkinter mijenja geometry size (window size) ovisno o tome koliko widgeta imamo

#root.columnconfigure(1, weight=2)
#root.rowconfigure(1, weight=2)


def check():
    username = username_entry.get()
    # ovako dohvacamo ono sto smo unijeli u entry u GUI
    password = password_entry.get()
    if username == "admin" and password == "0000":
        login_label.config(text="Login successful !", fg="green")
    else:
        login_label.config(text="Login failed !", fg="red")






username_label = tk.Label(root, text="Username", font=("Arial", 15))
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

password_label = tk.Label(root, text="Password", font=("Arial", 15))
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
 
login_button = tk.Button(root, text="Login", command=check)  # login buttoin namjestiti da bude disabled sve dok ne upisem osifru ili username
login_button.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

login_label = tk.Label(root, text="", )
login_label.grid(row=3, column=1, padx=10, pady=10, columnspan=2)



"""
#PRIMJER S NETA:
fields = {}

fields['username_label'] = ttk.Label(text='Username:')
fields['username'] = ttk.Entry()

fields['password_label'] = ttk.Label(text='Password:')
fields['password'] = ttk.Entry(show="*")


for field in fields.values():
    field.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

ttk.Button(text='Login').pack(anchor=tk.W, padx=10, pady=5)
"""

root.mainloop()