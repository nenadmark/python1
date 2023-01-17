import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Algebra / TKINTER EVENTS")
root.geometry("600x400")
root.resizable(0, 0) # sprijecen je resize windowa po x osi i po y osi


unsena_slova = ""
# kada ove event handler funkcije zovemo, moraju prvi argument primiti event ( koji event ce zvati ) ( u ovom slucaju )
def on_keypress(event):
    global unsena_slova
    unsena_slova += event.char


    # tu na primjer odmah dohvacamo sto tipkamo na tipkovnici pomocu on_keypress funkcije koja se triggera dolje u kodu, ona se trigerra bilo kojim keyem 
    #print(event.char)
    text_label_varijabla.set(unsena_slova)

def on_button2_click(event):
    

    

text_label = tk.Label(root, text="ovdje ce se prikazivati unesena slova.")
text_label.grid(row=0, column=0, pady=20)
c

text_label_varijabla = tk.StringVar()
# ovo je tkinterova varijabla, ona moze mijenjati vrijednost text_label_2
text_label_varijabla.set("bla bla bla")


# ovako mozemo direktno mijenjati text jednog labela 
text_label_2 = text_label = tk.Label(root, textvariable=text_label_varijabla)
text_label_2.grid(row=2, column=0, pady=20)


text_entry = tk.Entry(root)
text_entry.grid(row=1, column=0, pady=20)

root.bind("<Key>", on_keypress)
root.bind("<Button2->", on_button2_click)


root.mainloop()