# @author: João Gabriel Cardoso
# @github: github.com/joaogabrielrc


import tkinter as tk

# Internal Module
from app.calculator import Calculator


if __name__ == "__main__":
    # Creating the window
    window = tk.Tk()
    calculator = Calculator(window)

    # Starting the calculator
    calculator.start()