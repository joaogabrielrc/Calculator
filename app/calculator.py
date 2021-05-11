# @author: João Gabriel Cardoso
# @github: github.com/joaogabrielrc

import tkinter as tk

from json import load as json_load

class Calculator(): 
    def __init__(self, window):
        self.window = window

        # Loading settings
        self.settings = self.load_settings()

        # Window settings
        self.window.title("Calculator")
        self.window.maxsize(width=320, height=430)
        self.window.minsize(width=320, height=430)
        self.window.geometry("+150+100")
        self.window["bg"] = self.settings["global"]["bg"]

        # Creating the input
        self.input_frame = tk.Frame(self.window, cnf=self.settings["global"])
        self.input_frame.pack()
        self.create_input_content()

        # Creating the buttons
        self.buttons_frame = tk.Frame(self.window, cnf=self.settings["global"])
        self.buttons_frame.pack()
        self.create_buttons_content()


    @staticmethod
    def load_settings():
        settings = json_load(open("./app/settings/settings.json"))
        return settings
    
    def create_input_content(self):
        self.entry = tk.Entry(self.input_frame, cnf=self.settings["input"])
        self.entry.focus()
        self.entry.insert(0,0)
        self.entry.pack()

    def create_buttons_content(self):

        # Creating the numbers of calculator
        self.btn_0 = tk.Button(self.buttons_frame, text=0, cnf=self.settings["buttons"]["numbers"])
        self.btn_1 = tk.Button(self.buttons_frame, text=1, cnf=self.settings["buttons"]["numbers"])
        
        # Adding the buttons
        self.btn_0.grid(row=0, column=0, padx=1, pady=1)
        self.btn_1.grid(row=0, column=1, padx=1, pady=1)
        

    def start(self):
        self.window.mainloop()