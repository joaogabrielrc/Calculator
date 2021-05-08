import tkinter as tk

class Calculator():
    def __init__(self, window):
        self.window = window

        # Calculator size
        self.window.maxsize(width=335, height=415)
        self.window.minsize(width=335, height=415)
        self.window.geometry("+250+150")

        # Background color
        self.window["bg"] = "#2a2a2a"

        # Input frame
        input_frame = tk.Frame()
        input_entry = tk.Entry(width=60, font=("Arial", 30), bg="#2a2a2a", fg="#fff", selectbackground="#3a3a3a", relief="flat", borderwidth=10, justify="right")
        input_entry.focus()
        input_entry.pack()

        # Buttons frame
        buttons_frame = tk.Frame()

        # Packing the frames
        input_frame.pack()
        buttons_frame.pack()



    def start(self):
        self.window.mainloop()