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
        self.window.maxsize(width=290, height=410)
        self.window.minsize(width=290, height=410)
        self.window.geometry("+150+100")
        self.window["bg"] = "#1a1a1a"

        # Creating the input
        self.input_frame = tk.Frame(self.window, bg="#1a1a1a")
        self.input_frame.pack()
        self.create_input_content()

        # Creating the buttons
        self.buttons_frame = tk.Frame(self.window, bg="#666666")
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
        self.entry.pack(padx=10, pady=20)

    def create_buttons_content(self):

        # Creating the calculator numbers
        self.settings["buttons"]["numbers"].update(self.settings["buttons"]["global"])

        self.btn_0 = tk.Button(self.buttons_frame, text=0, cnf=self.settings["buttons"]["numbers"])
        self.btn_1 = tk.Button(self.buttons_frame, text=1, cnf=self.settings["buttons"]["numbers"])
        self.btn_2 = tk.Button(self.buttons_frame, text=2, cnf=self.settings["buttons"]["numbers"])
        self.btn_3 = tk.Button(self.buttons_frame, text=3, cnf=self.settings["buttons"]["numbers"])
        self.btn_4 = tk.Button(self.buttons_frame, text=4, cnf=self.settings["buttons"]["numbers"])
        self.btn_5 = tk.Button(self.buttons_frame, text=5, cnf=self.settings["buttons"]["numbers"])
        self.btn_6 = tk.Button(self.buttons_frame, text=6, cnf=self.settings["buttons"]["numbers"])
        self.btn_7 = tk.Button(self.buttons_frame, text=7, cnf=self.settings["buttons"]["numbers"])
        self.btn_8 = tk.Button(self.buttons_frame, text=8, cnf=self.settings["buttons"]["numbers"])
        self.btn_9 = tk.Button(self.buttons_frame, text=9, cnf=self.settings["buttons"]["numbers"])
        

        # Creating the calculator operations 
        self.settings["buttons"]["operations"].update(self.settings["buttons"]["global"])
        self.settings["buttons"]["equal"].update(self.settings["buttons"]["global"])

        self.btn_C = tk.Button(self.buttons_frame, text="C", cnf=self.settings["buttons"]["operations"])
        self.btn_open = tk.Button(self.buttons_frame, text="(", cnf=self.settings["buttons"]["operations"])
        self.btn_close = tk.Button(self.buttons_frame, text=")", cnf=self.settings["buttons"]["operations"])
        self.btn_del = tk.Button(self.buttons_frame, text="<", cnf=self.settings["buttons"]["operations"])
        self.btn_add = tk.Button(self.buttons_frame, text="+", cnf=self.settings["buttons"]["operations"])
        self.btn_subtract = tk.Button(self.buttons_frame, text="-", cnf=self.settings["buttons"]["operations"])
        self.btn_multiply = tk.Button(self.buttons_frame, text="*", cnf=self.settings["buttons"]["operations"])
        self.btn_share = tk.Button(self.buttons_frame, text="/", cnf=self.settings["buttons"]["operations"])
        self.btn_point = tk.Button(self.buttons_frame, text=".", cnf=self.settings["buttons"]["operations"])
        self.btn_equal = tk.Button(self.buttons_frame, text="=", cnf=self.settings["buttons"]["equal"])


        # First row    
        self.btn_C.grid(row=0, column=0, padx=1, pady=1)
        self.btn_open.grid(row=0, column=1, padx=1, pady=1)
        self.btn_close.grid(row=0, column=2, padx=1, pady=1)
        self.btn_del.grid(row=0, column=3, padx=1, pady=1)
        # Second row
        self.btn_7.grid(row=1, column=0, padx=1, pady=1)
        self.btn_8.grid(row=1, column=1, padx=1, pady=1)
        self.btn_9.grid(row=1, column=2, padx=1, pady=1)
        self.btn_add.grid(row=1, column=3, padx=1, pady=1)
        # Third row
        self.btn_4.grid(row=2, column=0, padx=1, pady=1)
        self.btn_5.grid(row=2, column=1, padx=1, pady=1)
        self.btn_6.grid(row=2, column=2, padx=1, pady=1)
        self.btn_subtract.grid(row=2, column=3, padx=1, pady=1)
        # Fourth row
        self.btn_1.grid(row=3, column=0, padx=1, pady=1)
        self.btn_2.grid(row=3, column=1, padx=1, pady=1)
        self.btn_3.grid(row=3, column=2, padx=1, pady=1)
        self.btn_multiply.grid(row=3, column=3, padx=1, pady=1)
        # Fifth place
        self.btn_point.grid(row=4, column=0, padx=1, pady=1)
        self.btn_0.grid(row=4, column=1, padx=1, pady=1)
        self.btn_share.grid(row=4, column=2, padx=1, pady=1)
        self.btn_equal.grid(row=4, column=3, padx=1, pady=1)
        

    def start(self):
        self.window.mainloop()