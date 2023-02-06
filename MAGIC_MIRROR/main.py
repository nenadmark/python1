import tkinter as tk
from app_settings import *
from clock.gui import LiveClock
from meteo.gui import LiveWeather
from other_API.gui import CovidTrack

if __name__=="__main__":

    root = tk.Tk()
    root.title("Algebra / Magic Mirror")
    root.config(bg=color_palette["primary"]) 
    #settings.color_palette.get("primary") > .get vraca value ako postoji, ako ne onda vraca None

    live_clock = LiveClock(root)
    #clock_update = LiveClock.update_clock(root)
    meteo = LiveWeather(root)

    covid = CovidTrack(root)
    
    root.mainloop()