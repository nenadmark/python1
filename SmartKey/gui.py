import tkinter as tk
from tkinter import *
from sqlalchemy import delete
from crud import login_user, get_all_users, delete_user


# 



class UsersList:
    def __init__(self, root):
        self.root = root
        self.listbox = tk.Listbox(self.root)
        self.listbox.grid(row=3, column=0, padx=10, pady=10)
        self.load_users()

        self.user_to_delete = None

    def load_users(self):
        users = get_all_users()

        for i, user in enumerate(users):
            frame = tk.Frame(self.listbox)
            frame.grid(row=7, column=0)
            user_label = tk.Label(frame, text=user.name)
            user_label.grid(row=i, column=0)
            delete_button = tk.Button(frame, text="delete", command=lambda: self.on_delete(user)) 
            delete_button.grid(row=i, column=1)
            self.listbox.insert(i, frame)

    def on_delete(self, user):
        delete_user(user.id)
        print("Korisnik obrisan iz baze.")

class LoginForm:
    def __init__(self, root):
        self.root = root
        #header = tk.Frame(root)
        #body = tk.Frame(root)
        #footer = tk.Frame(root)
        self.login_button = tk.Button(root, text="RING", command=self.on_ring)
        self.login_button.grid(row=0, column=1, padx=20, pady=20, columnspan=2)

        self.login_button = tk.Button(root, text="UNLOCK", command=self.on_unlock)
        self.login_button.grid(row=0, column=3, padx=180, pady=20, columnspan=2)


        self.num0_1 = tk.Button(root, text=" ")
        self.num0_1.grid(row=2, column=0, padx=10, pady=10)

        self.num0_4 = tk.Label(root, text="STATUS", height=20, width=30)
        self.num0_4.grid(row=2, column=3, padx=10, pady=1)

        self.num1 = tk.Button(root, text="1", height=3, width=3, command=lambda:self.on_num(self.num1.cget('text')))
        self.num1.grid(row=3, column=0, padx=10, pady=10)
        self.num2 = tk.Button(root, text="2", height=3, width=3, command=lambda:self.on_num(self.num2.cget('text')))
        self.num2.grid(row=3, column=1, padx=10, pady=10)
        self.num3 = tk.Button(root, text="3", height=3, width=3, command=lambda:self.on_num(self.num3.cget('text')))
        self.num3.grid(row=3, column=2, padx=10, pady=10)
        self.num4 = tk.Button(root, text="4", height=3, width=3, command=lambda:self.on_num(self.num4.cget('text')))
        self.num4.grid(row=4, column=0, padx=10, pady=10)
        self.num5 = tk.Button(root, text="5", height=3, width=3, command=lambda:self.on_num(self.num5.cget('text')))
        self.num5.grid(row=4, column=1, padx=10, pady=10)
        self.num6 = tk.Button(root, text="6", height=3, width=3, command=lambda:self.on_num(self.num6.cget('text')))
        self.num6.grid(row=4, column=2, padx=10, pady=10)
        self.num7 = tk.Button(root, text="7", height=3, width=3, command=lambda:self.on_num(self.num7.cget('text')))
        self.num7.grid(row=5, column=0, padx=10, pady=10)
        self.num8 = tk.Button(root, text="8", height=3, width=3, command=lambda:self.on_num(self.num8.cget('text')))
        self.num8.grid(row=5, column=1, padx=10, pady=10)
        self.num9 = tk.Button(root, text="9", height=3, width=3, command=lambda:self.on_num(self.num9.cget('text')))
        self.num9.grid(row=5, column=2, padx=10, pady=10)
        self.num0_5 = tk.Button(root, text=" ", height=3, width=3)
        self.num0_5.grid(row=6, column=0, padx=10, pady=10)
        self.num0 = tk.Button(root, text="0", height=3, width=3, command=lambda:self.on_num(self.num0.cget('text')))
        self.num0.grid(row=6, column=1, padx=10, pady=10)
        self.numC = tk.Button(root, text="C", height=3, width=3, command=lambda:self.on_num(self.numC.cget('text')))
        self.numC.grid(row=6, column=2, padx=10, pady=10)
    
    keys=[]
    def on_num(self, text):
        keys = self.keys
        if text == "C":
            keys.pop()
            print(keys)
        else:
            keys.append(text)
            print(keys)
        
    def on_ring(self):
        self.num0_4["text"] = "Ring is active!\n Someone will soon \n open door."

    def on_unlock(self):
        keys = self.keys
        keys_len = len(keys)
        if keys:
            if keys_len == 4:
                self.num0_4["text"] = "Unlocked for user: ('in progress')"
                #self.num0_1.config(self.root,bg="green")

                if keys[0] == "0" and keys[1] == "0" and keys[2] == "0" and keys[3] == "0":
                    self.num0_4["text"] = "Admin login successful!"
            else:
                self.num0_4["text"] = "Locked - wrong input"
        else:
            self.num0_4["text"] = "Locked - wrong input"