# @author: João Gabriel Cardoso
# @github: github.com/joaogabrielrc

class Calculator(): 
    def __init__(self, window):
        self.window = window

        # Window settings
        self.window.title("Calculator")
        self.window.maxsize(width=320, height=430)
        self.window.minsize(width=320, height=430)
        self.window.geometry("+150+100")
        self.window["bg"] = "#1a1a1a"
        
    def start(self):
        self.window.mainloop()