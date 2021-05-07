# Author: João Gabriel Cardoso
# GitHub: github.com/joaogabrielrc



# Módulo interno
from .calculation import Calculation

# Módulo json 
from json import load as json_load

class Calculator():
    def __init__(self, window):
        self.window = window
        self.calculation = Calculation()

        self.settings = self.load_settings()
        print(self.settings)

    # Metódo estático para carregar configurações da calculadora
    @staticmethod
    def load_settings():
        settings = json_load(open("./app/settings/settings.json")) 
        return settings

    def start(self):
        self.window.mainloop()
        