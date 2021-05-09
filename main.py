
import tkinter as tk

class Calculator():
    def __init__(self, window):
        self.window = window


        # Window settings
        self.window.title("Calculator")
        self.window.maxsize(width=320, height=430)
        self.window.minsize(width=320, height=430)
        self.window.geometry("+150+100")
        self.window["bg"] = "#1a1a1a"


        # Creating the input
        self.input_frame = tk.Frame()
        self.input_content()


        # Creating the buttons
        self.buttons_frame = tk.Frame()
        self.buttons_content()


        # Packing the frames
        self.input_frame.pack()
        self.buttons_frame.pack()
        
    def start():
        window.mainloop()

    def input_content(self):
        input_entry = tk.Entry(
                master=self.input_frame, 
                font=("Arial", 40), 
                width=60, 
                bg="#1a1a1a", 
                fg="#fff", 
                justify="right", 
                relief="flat",
                borderwidth=10
            )
        input_entry.focus()
        input_entry.pack()

    def buttons_content(self):
        button_0 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="C"
        )
        button_0.grid(row=0, column=0)

        button_1 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="("
        )
        button_1.grid(row=0, column=1)

        button_2 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text=")"
        )
        button_2.grid(row=0, column=2)

        button_3 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="<"
        )
        button_3.grid(row=0, column=3)

        button_4 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="7"
        )
        button_4.grid(row=1, column=0)

        button_5 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="8"
        )
        button_5.grid(row=1, column=1)

        button_6 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="9"
        )
        button_6.grid(row=1, column=2)

        button_7 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="/"
        )
        button_7.grid(row=1, column=3)

        button_8 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="6"
        )
        button_8.grid(row=2, column=0)

        button_9 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="5"
        )
        button_9.grid(row=2, column=1)

        button_10 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="4"
        )
        button_10.grid(row=2, column=2)

        button_11 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="x"
        )
        button_11.grid(row=2, column=3)

        button_12 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="1"
        )
        button_12.grid(row=3, column=0)

        button_13 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="2"
        )
        button_13.grid(row=3, column=1)

        button_14 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="3"
        )
        button_14.grid(row=3, column=2)

        button_15 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="-"
        )
        button_15.grid(row=3, column=3)

        button_16 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="."
        )
        button_16.grid(row=4, column=0)

        button_17 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="0"
        )
        button_17.grid(row=4, column=1)

        button_18 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="="
        )
        button_18.grid(row=4, column=2)

        button_19 = tk.Button(
            master=self.buttons_frame, 
            font=("Arial Black", 11),
            width=6,
            height=2,
            bg="#0a0a0a", 
            fg="#fff",
            text="+"
        )
        button_19.grid(row=4, column=3)

# Creating the window
window = tk.Tk()
Calculator(window)


# Starting the calculator
Calculator.start()