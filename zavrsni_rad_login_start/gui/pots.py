import tkinter as tk

class PotsFrame:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)

        self.create_living_room_label()
        self.create_bedroom_label()
        self.create_kitchen_label()
        self.create_toilet_label()
        self.create_on_button_1()
        self.create_off_button_1()
        self.create_on_button_2()
        self.create_off_button_2()
        self.create_on_button_3()
        self.create_off_button_3()
        self.create_on_button_4()
        self.create_off_button_4()
        self.create_change_color_button_1()
        self.create_change_color_button_2()
        self.create_change_color_button_3()
        self.create_change_color_button_4()
        self.create_change_intensity_slider_1()
        self.create_change_intensity_slider_2()
        self.create_change_intensity_slider_3()
        self.create_change_intensity_slider_4()

       
    def create_living_room_label(self):
        self.living_room_label = tk.Label(self.frame, text="Living room")
        self.living_room_label.grid(row=0, column=0, padx=10, pady=10)

    def create_bedroom_label(self):
        self.bedroom_label = tk.Label(self.frame, text="Bedroom")
        self.bedroom_label.grid(row=1, column=0, padx=10, pady=10)

    def create_kitchen_label(self):
        self.kitchen_label = tk.Label(self.frame, text="Kitchen")
        self.kitchen_label.grid(row=2, column=0, padx=10, pady=10)

    def create_toilet_label(self):
        self.toilet_label = tk.Label(self.frame, text="Toilet")
        self.toilet_label.grid(row=3, column=0, padx=10, pady=10)


    def create_on_button_1(self):
        self.on_button = tk.Button(self.frame, text="Turn on")
        self.on_button.grid(row=0, column=1, padx=10, pady=10)
   
    def create_off_button_1(self):
        self.off_button = tk.Button(self.frame, text= "Turn off")
        self.off_button.grid(row=0, column=2, padx=10, pady=10)

    def create_change_color_button_1(self):
        self.change_color_button_1 = tk.Button(self.frame, text= "Change color")
        self.change_color_button_1.grid(row=0, column=3, padx=10, pady=10)

    def create_change_intensity_slider_1(self):
        self.change_intensity_slider_1 = tk.Scale(self.frame, from_=0,
            to=100, orient='horizontal')
        self.change_intensity_slider_1.grid(row=0, column=4, padx=10, pady=10)


    def create_on_button_2(self):
        self.on_button = tk.Button(self.frame, text="Turn on")
        self.on_button.grid(row=1, column=1, padx=10, pady=10)
   
    def create_off_button_2(self):
        self.off_button = tk.Button(self.frame, text= "Turn off")
        self.off_button.grid(row=1, column=2, padx=10, pady=10)

    def create_change_color_button_2(self):
        self.change_color_button_2 = tk.Button(self.frame, text= "Change color")
        self.change_color_button_2.grid(row=1, column=3, padx=10, pady=10)
    
    def create_change_intensity_slider_2(self):
        self.change_intensity_slider_2 = tk.Scale(self.frame, from_=0,
            to=100, orient='horizontal')
        self.change_intensity_slider_2.grid(row=1, column=4, padx=10, pady=10)


    def create_on_button_3(self):
        self.on_button = tk.Button(self.frame, text="Turn on")
        self.on_button.grid(row=2, column=1, padx=10, pady=10)
   
    def create_off_button_3(self):
        self.off_button = tk.Button(self.frame, text= "Turn off")
        self.off_button.grid(row=2, column=2, padx=10, pady=10)

    def create_change_color_button_3(self):
        self.change_color_button_3 = tk.Button(self.frame, text= "Change color")
        self.change_color_button_3.grid(row=2, column=3, padx=10, pady=10)

    def create_change_intensity_slider_3(self):
        self.change_intensity_slider_3 = tk.Scale(self.frame, from_=0,
            to=100, orient='horizontal')
        self.change_intensity_slider_3.grid(row=2, column=4, padx=10, pady=10)


    def create_on_button_4(self):
        self.on_button = tk.Button(self.frame, text="Turn on")
        self.on_button.grid(row=3, column=1, padx=10, pady=10)
   
    def create_off_button_4(self):
        self.off_button = tk.Button(self.frame, text= "Turn off")
        self.off_button.grid(row=3, column=2, padx=10, pady=10)

    def create_change_color_button_4(self):
        self.change_color_button_4 = tk.Button(self.frame, text= "Change color")
        self.change_color_button_4.grid(row=3, column=3, padx=10, pady=10)
        
    def create_change_intensity_slider_4(self):
        self.change_intensity_slider_4 = tk.Scale(self.frame, from_=0,
            to=100, orient='horizontal')
        self.change_intensity_slider_4.grid(row=3, column=4, padx=10, pady=10)