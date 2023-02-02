import datetime as dt
import tkinter as tk

from app_settings import *


class LiveClock:
    def __init__(self, parent):
        self.parent = parent
        self.dt_label = tk.Label(
            self.parent,
            font=(default_font, 20),
            text="",
            bg=color_palette["primary"],
            fg=color_palette["text"]
            )
        self.dt_label.grid(row=0, column=0, padx=10, pady=10)
        self.update_clock()
    
    def update_clock(self):
        current_dt = dt.datetime.now().strftime(date_format)
        self.dt_label.config(text=current_dt)
        self.dt_label.after(1000, self.update_clock)