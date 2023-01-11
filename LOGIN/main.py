import tkinter as tk
from gui import LoginForm

#print("bla")

# tu kreiramo glavnu stvar 
if __name__=="__main__":
    # ovdje kreiramo root, parenta za tkinter
    root= tk.Tk()
    root.title("Login App")

    login_form = LoginForm(root)
    # TU INSTANCIRAMO FORMU IZ GUI.PY
    # login forma prilikom instanciranja prima root windowa iz gui.py

    # mainloop zapravo u loopu prikazuje sve na ekran
    root.mainloop()

# ako smo pokrenuli skriptu u pythonu, onda python stavlja __name__ kao da je __main__
# ovaj print u ifu ce se pokrenuti samo ako pokrenemo main kao skripu
# POKRECEMO MAIN.PY 
# elemente GUI-a dodajemo u gui.py