# tkinter module
import tkinter as tk

# internal module
from app.calculator import Calculator

# if the current file name is the same as the the main file name do
if __name__ == '__main__':
    # Creating the window
    window = tk.Tk()
    
    calculator = Calculator(window)
    calculator.start()