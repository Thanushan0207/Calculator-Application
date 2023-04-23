import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        self.total = tk.DoubleVar()
        self.entered_number = tk.StringVar()
        self.entered_number.set('0')
        
        self.total_label = tk.Label(master, textvariable=self.total)
        self.total_label.grid(row=0, column=0, columnspan=4, sticky="W", padx=5, pady=5)
        
        self.entry = tk.Entry(master, textvariable=self.entered_number, font=('Helvetica', 20), width=12,
                             borderwidth=5)
        self.entry.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        
        self.create_button("1", 2, 0)
        self.create_button("2", 2, 1)
        self.create_button("3", 2, 2)
        self.create_button("4", 3, 0)
        self.create_button("5", 3, 1)
        self.create_button("6", 3, 2)
        self.create_button("7", 4, 0)
        self.create_button("8", 4, 1)
        self.create_button("9", 4, 2)
        self.create_button("0", 5, 0)
        self.create_button("C", 5, 1)
        self.create_button("=", 5, 2)
        self.create_button("+", 2, 3)
        self.create_button("-", 3, 3)
        self.create_button("*", 4, 3)
        self.create_button("/", 5, 3)
        
    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, font=('Helvetica', 20), width=5, height=2,
                          command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)
        
    def button_click(self, text):
        if text == "=":
            try:
                self.total.set(eval(self.entered_number.get()))
                self.entered_number.set("0")
            except:
                self.total.set("Error")
                self.entered_number.set("0")
        elif text == "C":
            self.total.set("0")
            self.entered_number.set("0")
        else:
            if self.entered_number.get() == "0":
                self.entered_number.set(text)
            else:
                self.entered_number.set(self.entered_number.get() + text)

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()