
import tkinter as tk

class Calculator():
    def __init__(self, window):
        self.window = window


        # Window settings
        self.window.title("Calculator")
        self.window.maxsize(width=350, height=500)
        self.window.minsize(width=350, height=500)
        self.window.geometry("+150+100")
        self.window["bg"] = "#222"


        # Creating the input
        self.input_frame = tk.Frame()
        self.input_content()


        # Packing the frames
        self.input_frame.pack()
        
    def start():
        window.mainloop()

    def input_content(self):
        input_entry = tk.Entry(
                master=self.input_frame, 
                font=("Arial", 40), 
                width=60, 
                bg="#222", 
                fg="#fff", 
                justify="right", 
                relief="flat",
                borderwidth=10
            )
        input_entry.focus()
        input_entry.pack()


# Creating the window
window = tk.Tk()
Calculator(window)


# Starting the calculator
Calculator.start()