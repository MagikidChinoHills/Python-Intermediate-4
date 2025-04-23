# Lesson: Making a Calculator with Python and Tkinter

# Today we're going to build a simple calculator using Python.
# This calculator can add and subtract two numbers. We'll use a cool tool called Tkinter
# that lets us build buttons, text boxes, and labels on a screen!

# Let's break this down step by step so it's super easy to understand.

# Step 1: Import the Tkinter Module
import tkinter as tk  # This brings in the tools we need to make windows and buttons.

# Step 2: Let's create the math functions!
def add(x, y):
    return x + y  # This adds two numbers and gives the answer back

# This function is used to subtract two numbers
def subtract(x, y):
    return x - y  # This subtracts the second number from the first

# Step 3: This function checks what math to do and shows the answer

def calculate():
    try:
        # Grab the numbers from the boxes and turn them into real numbers
        num1 = float(entry_num1.get())  # .get() takes the text typed into the entry box
        num2 = float(entry_num2.get())
        op = operation.get()  # Check if the user chose '+' or '-'

        # Do the right math based on the choice
        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)

        # Show the result on the screen
        update_result_label("Result: " + str(result))
    except ValueError:
        # If they didn't type a number, tell them it was wrong
        update_result_label("Invalid input")

# Step 4: Function to update the label with the result

def update_result_label(message):
    result_label.config(text=message)  # .config() changes the text on the label

# Step 5: Function to clear everything and start fresh

def clear():
    entry_num1.delete(0, tk.END)  # .delete() clears the entry box from start (0) to end
    entry_num2.delete(0, tk.END)
    update_result_label("Result:")

# Step 6: Create the main window
root = tk.Tk()  # Makes the app window
root.title("Enhanced Calculator")  # Sets the window title

# Step 7: Add the text boxes to type numbers
entry_num1 = tk.Entry(root, width=10)  # tk.Entry makes a box where you can type numbers
entry_num2 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=5, pady=5)  # .grid() tells the computer where to place the box
entry_num2.grid(row=0, column=2, padx=5, pady=5)

# Step 8: Add the dropdown to pick + or -
operation = tk.StringVar(root)  # StringVar is a special container that holds the dropdown value
operation.set("+")  # Default is addition
operation_menu = tk.OptionMenu(root, operation, "+", "-")  # This makes the dropdown menu
operation_menu.grid(row=0, column=1, padx=5, pady=5)

# Step 9: Add the Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate)  # Button that does math when clicked
calc_button.grid(row=1, column=0, padx=5, pady=5)

# Step 10: Add the Clear button
clear_button = tk.Button(root, text="Clear", command=clear)  # Button that clears everything when clicked
clear_button.grid(row=2, column=0, padx=5, pady=5)

# Step 11: Add a label to show the answer
result_label = tk.Label(root, text="Result:")  # Label is a text display for the answer
result_label.grid(row=3, columnspan=3, padx=5, pady=5)  # columnspan=3 means the label stretches across 3 columns

# Step 12: Keep the window open!
root.mainloop()  # This keeps everything showing and lets us click buttons!

# Function Explanations:
# - .get(): gets the text from an entry box
# - .delete(start, end): clears text from entry box
# - .config(): changes things like text or color of a widget
# - .grid(): places things (buttons, boxes, etc.) in a table-like layout
# - StringVar(): holds and updates a string value (used with dropdowns)
# - mainloop(): starts the app and waits for the user to do stuff (like click!)

# That's it! You've just built a real calculator with Python. Great job!
