# Author: João Gabriel Cardoso
# GitHub: github.com/joaogabrielrc



# Módulo tkinter
import tkinter as tk
# Módulo interno
from app.calculator import Calculator

if __name__ == '__main__':
    window = tk.Tk()
    calculator = Calculator(window)
    # calculator.start()
