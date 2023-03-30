import tkinter as tk

class PotsFrame:
    def __init__(self, parent, session):
        self.session = session
        self.frame = tk.Frame(parent)
        self.font = ("TimesNewRoman", 10, "bold")
        self.frame.config(bg="palegreen1")

        self.create_pots_frame()

    pots_data = [
    {
        'id': '001',
        'name': 'Pot 1',
        'plant_inside': 'Plant 1',
        'image_path': 'assets\\thumbs\pots\Carlos_Pot_Green_130x130.png'
    },
    {
        'id': '002',
        'name': 'Pot 2',
        'plant_inside': 'Plant 2',
        'image_path': 'assets\\thumbs\pots\Lexi_Pot_Black_130x130.png'
    },
    {
        'id': '003',
        'name': 'Pot 3',
        'plant_inside': 'Plant 3',
        'image_path': 'assets\\thumbs\pots\Pablo_Basket_Jute_Cream_130x130.png'
    },
    {
        'id': '004',
        'name': 'Pot 4',
        'plant_inside': 'Plant 4',
        'image_path': 'assets\\thumbs\pots\Penny_Pot_Dark_Grey_130x130.png'
    },
    {
        'id': '005',
        'name': 'Pot 5',
        'plant_inside': 'Plant 5',
        'image_path': 'assets\\thumbs\pots\Stan_Pot_Dark_Green_1_130x130.png'
    },
    {
        'id': '006',
        'name': 'Pot 6',
        'plant_inside': 'Plant 6',
        'image_path': 'assets\\thumbs\pots\Stu_Pot_Green_130x130.png'
    }]

    def create_pots_frame(self):
        for i, pot in enumerate(self.pots_data):

            self.pot_frame = tk.LabelFrame(
                self.frame, text=pot['name'], width=450, height=140,
                font=self.font)
            self.pot_frame.grid(row=i, column=0, padx=10, pady=1, ipadx=60, ipady=1)
            self.pot_frame.config(bg="palegreen1")




            # Create a label to display the plant image
            image = tk.PhotoImage(file=pot['image_path'])
            image.configure(width=120, height=120)
            label_image = tk.Label(self.pot_frame, image=image, font=self.font)
            label_image.image = image
            label_image.grid(row=i, column=0, padx=7, pady=7)
        
            # Create labels to display the plant name, humidity, and temperature
            label_name = tk.Label(self.pot_frame, text=pot['id'], font=self.font)
            label_name.grid(row=i, column=1, padx=10)
            label_name.config(bg="palegreen1")
        
            label_humidity = tk.Label(self.pot_frame, text=f'Name: {pot["name"]}', font=self.font)
            label_humidity.grid(row=i, column=2, padx=10)
            label_humidity.config(bg="palegreen1")
        
            label_temperature = tk.Label(self.pot_frame, text=f'Plant inside: {pot["plant_inside"]}', font=self.font)
            label_temperature.grid(row=i, column=3, padx=10)
            label_temperature.config(bg="palegreen1")