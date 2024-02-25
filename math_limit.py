# The code snippet creates a GUI application using tkinter that allows users to calculate limits of mathematical expressions. It includes text entry fields for the symbol, limit, and expression, a calculate button, a result label, and a mode switch button for dark and light
import tkinter as tk
import sympy as sp

class LimitCalculator:
    def __init__(self):
        # Initialize the tkinter root widget
        self.root = tk.Tk()
        self.root.title('Limit Calculator')
        self.root.geometry('400x450')  # Set window size
        self.root.config(bg='black')  # Set default background color to black

        # Set the weight option for all the widgets
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight =1)

        # Create StringVar variables for each text entry
        self.symbol_var = tk.StringVar()
        self.limit_var = tk.StringVar()
        self.expression_var = tk.StringVar()

        # Create and position the symbol label and text entry
        self.symbol_label = tk.Label(self.root, text='Symbol', font=('Arial', 14), bg='black', fg='white')
        self.symbol_label.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')
        self.symbol_text = tk.Entry(self.root, textvariable=self.symbol_var, font=('Arial', 14), bg='black', fg='white', insertbackground='white')
        self.symbol_text.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

        # Create and position the limit label and text entry
        self.limit_label = tk.Label(self.root, text='Limit', font=('Arial', 14), bg='black', fg='white')
        self.limit_label.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        self.limit_text = tk.Entry(self.root, textvariable=self.limit_var, font=('Arial', 14), bg='black', fg='white', insertbackground='white')
        self.limit_text.grid(row=1, column=1, padx=20, pady=20, sticky='nsew')

        # Create and position the expression label and text entry
        self.expression_label = tk.Label(self.root, text='Expression', font=('Arial', 14), bg='black', fg='white')
        self.expression_label.grid(row=2, column=0, padx=20, pady=20, sticky='nsew')
        self.expression_text = tk.Entry(self.root, textvariable=self.expression_var, font=('Arial', 14), bg='black', fg='white', insertbackground='white')
        self.expression_text.grid(row=2, column=1, padx=20, pady=20, sticky='nsew')

        # Create and position the calculate button
        self.calculate_button = tk.Button(self.root, text='Calculate Limit', command=self.calculate_limit, font=('Arial', 14), bg='black', fg='white', state='disabled')
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')

        # Create and position the result label
        self.result_label = tk.Label(self.root, text='Result will be displayed here', font=('Arial', 14), bg='black', fg='white', wraplength=350)
        self.result_label.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

        # Create and position the mode switch button
        self.mode_button = tk.Button(self.root, text='🌞', command=self.switch_mode, font=('Arial', 14), bg='black', fg='white')
        self.mode_button.grid(row=5, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')

        # Initialize the symbol and limit variables
        self.sym = None
        self.lim = None

        # Initialize the mode variable
        self.dark_mode = True

        # Trace the text variables
        self.symbol_var.trace('w', lambda *args: self.check_entries())
        self.limit_var.trace('w', lambda *args: self.check_entries())
        self.expression_var.trace('w', lambda *args: self.check_entries())

        # Start the tkinter main loop
        self.root.mainloop()

    def calculate_limit(self):
        # Try to calculate the limit
        try:
            # Get the symbol from the text entry and convert it to a sympy Symbol
            self.sym = sp.Symbol(self.symbol_text.get())

            # Get the expression from the text entry
            expression = self.expression_text.get()

            # If the expression contains 'Sum', convert it to a sympy expression and call doit() if it's a Sum instance
            if 'Sum' in expression:
                expression = sp.sympify(expression)
                if isinstance(expression, sp.Sum):
                    expression = expression.doit()
            else:
                # If the expression doesn't contain 'Sum', just convert it to a sympy expression
                expression = sp.sympify(expression)

            # Calculate the limit and update the result label
            self.lim = sp.limit(expression, self.sym, self.limit_text.get())
            self.result_label.config(text=str(self.lim))
        except Exception as e:
            # If an error occurred during the calculation, update the result label with the error message
            self.result_label.config(text=f"Error: {str(e)}")

    def switch_mode(self):
        # Switch between Dark Mode and Light Mode
        if self.dark_mode:
            # If currently in Dark Mode, switch to Light Mode
            self.root.config(bg='white')
            self.symbol_label.config(bg='white', fg='black')
            self.symbol_text.config(bg='white', fg='black', insertbackground='black')
            self.limit_label.config(bg='white', fg='black')
            self.limit_text.config(bg='white', fg='black', insertbackground='black')
            self.expression_label.config(bg='white', fg='black')
            self.expression_text.config(bg='white', fg='black', insertbackground='black')
            self.calculate_button.config(bg='white', fg='black')
            self.result_label.config(bg='white', fg='black')
            self.mode_button.config(text='🌙', bg='white', fg='black')
            self.dark_mode = False
        else:
            # If currently in Light Mode, switch to Dark Mode
            self.root.config(bg='black')
            self.symbol_label.config(bg='black', fg='white')
            self.symbol_text.config(bg='black', fg='white', insertbackground='white')
            self.limit_label.config(bg='black', fg='white')
            self.limit_text.config(bg='black', fg='white', insertbackground='white')
            self.expression_label.config(bg='black', fg='white')
            self.expression_text.config(bg='black', fg='white', insertbackground='white')
            self.calculate_button.config(bg='black', fg='white')
            self.result_label.config(bg='black', fg='white')
            self.mode_button.config(text='🌞', bg='black', fg='white')
            self.dark_mode = True

    def check_entries(self):
        # Enable or disable the calculate button based on whether all text entries are filled
        if self.symbol_var.get() and self.limit_var.get() and self.expression_var.get():
            self.calculate_button.config(state='normal')
        else:
            self.calculate_button.config(state='disabled')

# Create an instance of the LimitCalculator class
LimitCalculator()