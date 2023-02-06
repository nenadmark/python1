import tkinter as tk
from app_settings import *
from .other_api import Covid

class CovidTrack:
    def __init__(self, parent) -> None:
        self.parent = parent

        self.cov_country = tk.Label(
            self.parent,
            font=(default_font, 20),
            text="Covid info - ",
            bg=color_palette["dark_primary_2"],
            fg=color_palette["text_2"]
            )
        self.cov_country.grid(row=5, column=0, padx=15, pady=15)
        
        self.cov_population = tk.Label(
            self.parent,
            font=(default_font, 15),
            text="Population: ",
            bg=color_palette["dark_primary_2"],
            fg=color_palette["text_2"]
            )
        self.cov_population.grid(row=7, column=0, padx=15, pady=15)
        
        self.cov_cases = tk.Label(
            self.parent,
            font=(default_font, 15),
            text="Cases:",
            bg=color_palette["dark_primary_2"],
            fg=color_palette["text_2"]
            )
        self.cov_cases.grid(row=8, column=0, padx=15, pady=15)

        self.cov_cases_new = tk.Label(
            self.parent,
            font=(default_font, 15),
            text="Cases Today:",
            bg=color_palette["dark_primary_2"],
            fg=color_palette["text_2"]
            )
        self.cov_cases_new.grid(row=9, column=0, padx=15, pady=15)
        
        self.cov_deaths = tk.Label(
            self.parent,
            font=(default_font, 15),
            text="Deaths:",
            bg=color_palette["dark_primary_2"],
            fg=color_palette["text_2"]
            )
        self.cov_deaths.grid(row=10, column=0, padx=15, pady=15)

        self.update_covid()

    def update_covid(self):
        data = Covid().get_Covid_values()
        #print("GUI data", data[0], data[1], data[2], data[3], data[4])

        self.cov_country.config(text=f"Covid info - {data[0]}")
        self.cov_population.config(text=f"Population: {data[1]}")
        self.cov_cases.config(text=f"Cases: {data[2]}")
        self.cov_deaths.config(text=f"Deaths: {data[3]}")
        self.cov_cases_new.config(text=f"Cases Today: {data[4]}")
        self.cov_country.after(60000, self.update_covid)