# Author: João Gabriel Cardoso
# GitHub: github.com/joaogabrielrc



import platform

import tkinter as tk

from json import load as json_load

from copy import deepcopy

# Módulo interno
from .calculation import Calculation

class Calculator():
    def __init__(self, window):
        self.window = window
        self.calculation = Calculation()


        # Criando metódo estático para carregar configurações da calculadora
        self.settings = self.load_settings()


        # Definindo o tema padrão de acordo com o sistema operacional
        if platform.system() == "Darwin":
            self.theme = self.get_theme("Default Theme For MacOS")
        else:
            self.theme = self.get_theme(self.settings["current_theme"])


        # Definindo as configurações da janela
        self.window.title("Calculator")
        self.window.maxsize(width=335, height=415)
        self.window.minsize(width=335, height=415)
        self.window.geometry("+250+100")
        self.window["bg"] = self.theme["window_bg"]


        # Área do input
        self.frame_input = tk.Frame(self.window, bg=self.theme["frame_bg"], pady=4)
        self.frame_input.pack()


        # Área dos botões
        self.frame_buttons = tk.Frame(self.window, bg=self.theme['frame_bg'], padx=2)
        self.frame_buttons.pack()


        # Funções para a criação dos conteúdos
        self.create_input(self.frame_input) 
        self.create_buttons(self.frame_buttons)

    @staticmethod
    def load_settings():
        settings = json_load(open("./app/settings/settings.json")) 
        return settings

    def get_theme(self, theme_name):
        
        list_of_themes = self.settings["themes"]

        theme_found = None
        for theme in list_of_themes:
            if theme_name == theme["name"]:
                theme_found = deepcopy(theme)
                break

        return theme_found

    def create_input(self, create_input):
        self.input = tk.Entry(create_input, cnf=self.theme["INPUT"]) 
        self.input.insert(0,0)
        self.input.pack()

    def create_buttons(self, frame_buttons):
        self.theme["BTN_NUMERICO"].update(self.settings["global"])
        self.BTN_NUM_0 = tk.Button(frame_buttons, text=0, cnf=self.theme["BTN_NUMERICO"])
        self.BTN_NUM_0.grid(row=4, column=1, padx=1, pady=1)
        

    def start(self):
        self.window.mainloop()
        