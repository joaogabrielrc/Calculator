# Author: João Gabriel Cardoso
# GitHub: github.com/joaogabrielrc


import tkinter as tk

# Internal module
from app.calculator import Calculator

if __name__ == "__main__":
    # Creating the window
    window = tk.Tk()    

    calculator = Calculator(window)

    # running the program
    calculator.start()