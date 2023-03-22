import tkinter as tk


#from tkinter import PhotoImage

#from assets import succulent_1


class PlantsFrame:
    def __init__(self, parent, session):
        self.session = session
        self.frame = tk.Frame(parent)
        self.font = ("TimesNewRoman", 15, "bold")
        self.frame.config(bg="skyblue")
        self.create_plants_frame()

    def create_plants_frame(self):
        # Create left and right frames
        left_frame = tk.Frame(self.frame, width=200, height=400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        right_frame = tk.Frame(self.frame, width=650, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)

        # Create frames and labels in left_frame
        tk.Label(left_frame, text="Plant Image").grid(row=0, column=0, padx=5, pady=5)

        # load image to be "edited"
        image = tk.PhotoImage(file="assets\succulent_1.png")
        original_image = image.subsample(3,3)  # resize image using subsample
        tk.Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)

        # Display image in right_frame
        tk.Label(right_frame, image=image).grid(row=0,column=0, padx=5, pady=5)

        # Create tool bar frame
        tool_bar = tk.Frame(left_frame, width=180, height=185)
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        # Example labels that serve as placeholders for other widgets
        tk.Label(tool_bar, text="info1", relief=tk.RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

        # Example labels that could be displayed under the "Tool" menu
        tk.Label(tool_bar, text="info1").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(tool_bar, text="info1").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(tool_bar, text="info1").grid(row=3, column=0, padx=5, pady=5)
