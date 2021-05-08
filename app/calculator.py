# Author: João Gabriel Cardoso
# GitHub: github.com/joaogabrielrc


import tkinter as tk

from json import load as json_load

class Calculator():
    def __init__(self, window):
        self.window = window


        # Calculator size
        self.window.maxsize(width=320, height=500)
        self.window.minsize(width=320, height=500)
        self.window.geometry("+250+150")


        # Background color
        self.window["bg"] = "#222"


        screen = tk.Entry(
                width=60, 
                font=('Arial', 30), 
                bg='#222', 
                fg='#fff', 
                selectbackground='#3a3a3a', 
                relief='flat', 
                borderwidth=10, 
                justify='right'
            )
        screen.focus()
        screen.pack()


        button_0 = tk.Button(
            text="(",
            width=4, 
            height=1,
            font=('Arial', 20), 
            bg='#1a1a1a', 
            fg='#fff', 
            relief='flat',
        )
        button_0.pack()
        
        button_1 = tk.Button(
            text=")",
            width=4, 
            height=1,
            font=('Arial', 20), 
            bg='#1a1a1a', 
            fg='#fff', 
            relief='flat',
        )
        button_1.pack()

    def start(self):
        self.window.mainloop()