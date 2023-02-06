import tkinter as tk
from app_settings import *
from .api import Meteo

class LiveWeather:
    def __init__(self, parent):
        self.parent = parent

        self.we_label_temp = tk.Label(
            self.parent,
            font=(default_font, 15),
            text="Temperature: ",
            bg=color_palette["dark_primary"],
            fg=color_palette["text_weather"]
            )
        self.we_label_temp.grid(row=1, column=0, padx=15, pady=15)
        
        self.we_label_code = tk.Label(
            self.parent,
            font=(default_font, 15),
            text="Weathercode: ",
            bg=color_palette["dark_primary"],
            fg=color_palette["text_weather"]
            )
        self.we_label_code.grid(row=2, column=0, padx=15, pady=15)
        
        self.we_label_wind = tk.Label(
            self.parent,
            font=(default_font, 15),
            text="Windspeed: ",
            bg=color_palette["dark_primary"],
            fg=color_palette["text_weather"]
            )
        self.we_label_wind.grid(row=4, column=0, padx=15, pady=15)

        self.we_label_dir = tk.Label(
            self.parent,
            font=(default_font, 15),
            text="Wind direction: ",
            bg=color_palette["dark_primary"],
            fg=color_palette["text_weather"]
            )
        self.we_label_dir.grid(row=3, column=0, padx=15, pady=15)

        self.update_weather()

    def update_weather(self):
        data = Meteo().get_Meteo_values()

        self.we_label_temp.config(text=f"Temperature: {data[0]} °C")
        self.we_label_wind.config(text=f"Windspeed: {data[1]} m/s")
        self.we_label_code.config(text=f"Weather Code: {data[2]}")
        self.we_label_dir.config(text=f"Wind direction: {data[3]}°")
        self.we_label_temp.after(60000, self.update_weather)