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
        'id': 'PT 1',
        'name': 'Pablo Basket Jute Cream',
        'radius': '14',
        'p_code': 'PL 1',
        'image_path': 'assets\\thumbs\pots\Pablo_Basket_Jute_Cream_130x130.png'
    },
    {
        'id': 'PT 2',
        'name': 'Stu Pot Green',
        'radius': '14',
        'p_code': 'PL 2',
        'image_path': 'assets\\thumbs\pots\Stu_Pot_Green_130x130.png'
    },
    {
        'id': 'PT 3',
        'name': 'Lexi Pot Black',
        'radius': '18',
        'p_code': 'PL 3',
        'image_path': 'assets\\thumbs\pots\Lexi_Pot_Black_130x130.png'
    },
    {
        'id': 'PT 4',
        'name': 'Penny Pot Dark Grey',
        'radius': '17 cm',
        'p_code': 'PL 4',
        'image_path': 'assets\\thumbs\pots\Penny_Pot_Dark_Grey_130x130.png'
    },
    {
        'id': 'PT 5',
        'name': 'Stan Pot Dark Green',
        'radius': '14 cm',
        'p_code': 'PL 5',
        'image_path': 'assets\\thumbs\pots\Stan_Pot_Dark_Green_1_130x130.png'
    },
    {
        'id': 'PT 6',
        'name': 'Carlos Pot Green',
        'radius': '13 cm',
        'p_code': 'PL 6',
        'image_path': 'assets\\thumbs\pots\Carlos_Pot_Green_130x130.png'
    }]

    def create_pots_frame(self):
        for i, pot in enumerate(self.pots_data):

            self.pot_frame = tk.LabelFrame(
                self.frame, text=f'{pot["id"]} - {pot["name"]}', width=450, height=140,
                font=self.font)
            self.pot_frame.grid(row=i, column=0, padx=5, pady=1, ipadx=60, ipady=1, sticky="w")
            self.pot_frame.config(bg="palegreen1")

            image = tk.PhotoImage(file=pot['image_path'])
            image.configure(width=120, height=120)
            label_image = tk.Label(self.pot_frame, image=image, font=self.font)
            label_image.image = image
            label_image.grid(row=i, column=0, padx=5, pady=7)
        
            label_name = tk.Label(self.pot_frame, text=f'Ø: {pot["radius"]}', font=self.font)
            label_name.grid(row=i, column=1, padx=5)
            label_name.config(bg="palegreen1")
        
            label_humidity = tk.Label(self.pot_frame, text=f'Name: {pot["name"]}', font=self.font)
            label_humidity.grid(row=i, column=2, padx=5)
            label_humidity.config(bg="palegreen1")
        
            label_temperature = tk.Label(self.pot_frame, text=f'Plant inside: {pot["p_code"]}', font=self.font)
            label_temperature.grid(row=i, column=3, padx=5)
            label_temperature.config(bg="palegreen1")