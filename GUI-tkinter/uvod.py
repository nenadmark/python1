import tkinter as tk
from tkinter import *

#razlika izmedju tk i ttk je:
    # funkcije koje ima su slicne zapravo
    # ttk modernije izgleda
    # tkinter originalni moze ici bolje za neke manje lijepe istarije aplikacije
    # ttk je napravljen da bi tkinter mogao pratiti nove GUI alate,
    # ttk je manje vise isto sto i tk samo modernije izgleda

root = tk.Tk()
root.title("python GUI uvod") #naziv prozora
root.geometry("600x400") # odredjuejmo velicinu tog prozora

######################################
# u argumentima kod konstruktora za klasu: 
# * znaci da primamo beskonacan broj argumenata, nebitno kako se nazivaju ti argumenti
# ** znaci da primamo beskonacan broj argumenata, TU JE bitno kako se argumenti kako zovu... 
#########################################
# https://www.pythontutorial.net/tkinter/tkinter-pack/#:~:text=Tkinter%20pack%20geometry%20manager%20example,ipady%20%2C%20padx%20%2C%20and%20pady%20.

# https://www.pythontutorial.net/tkinter/tkinter-grid/

count_label = tk.Label(root, text=0, font=("Arial", 30))
count_label.grid(column=0, row=1)


count = 0
def on_button_click():
    # s globalom tu kazemo pythonu da se ovaj count odnosi na onu globalnu varijablu iznad, te ju uvecaj za jedan i ispisi
    global count
    count += 1

    #ovako cemo sada mijenjati s tom funkcijom vrijednost texta pomocu config funkcije koju tkinter ima

    count_label.config(text=count)
    if count >= 5:
        button2.config(state=NORMAL)

on_button_click()





# dodavanje buttona
button1 = tk.Button(root, text="button1", fg="red", padx="25", pady="25", command=on_button_click)
# pri pozivanju funkcije na click, tu ne pozivamo funkciju, vec tkintera navodimo da on nju sam pokrene

#button1.pack()
button1.grid(padx="10", pady="10")

button2 = tk.Button(root, text="button2", fg="red", padx="25", pady="25", state=DISABLED)
#button1.pack()
button2.grid(padx="10", pady="10")

count_label = tk.Label(root, text=0, font=("Arial", 30))
count_label.grid(column=0, row=1)






"""
button2 = tk.Button(root, text="button2", bg="green")
button2.pack(side=tk.BOTTOM )

button3 = tk.Button(root, text="button3")
button3.pack(side=tk.LEFT)

button4 = tk.Button(root, text="button4")
button4.pack(side=tk.RIGHT)
"""



"""def print_msg():
   Label(root, text="Hello World!", font=('11')).pack()

root.bind("<Return>", lambda e: print_msg())
buttonq = Button(root, text="Click Me", command=print_msg)
buttonq.pack()"""




root.mainloop() # pozivamo tu glavnu petlju