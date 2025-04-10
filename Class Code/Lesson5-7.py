Welcome to the Tkinter class! In these notes, you'll learn how to create simple programs with windows, buttons,
and drawings using Python's Tkinter module. We cover three projects:

1. Animated Area Calculator
2. Simple Pong Game
3. To-Do List Application

-------------------------------------------------------------------------------
Table of Contents
-------------------------------------------------------------------------------
1. Introduction to Tkinter
2. Lesson 5: Animated Area Calculator
   - Setup and Imports
   - Calculating the Area
   - Dynamic UI for Dimensions
   - Drawing and Animating the Shape
3. Lesson 6: Simple Pong Game
   - Game Window and Canvas
   - Drawing the Paddles and Ball
   - Animating the Ball
   - Moving the Paddles
4. Lesson 7: To-Do List Application
   - Setup and GUI Layout
   - Task Management Functions
   - Building and Updating the List
5. Final Thoughts

-------------------------------------------------------------------------------
1. Introduction to Tkinter
-------------------------------------------------------------------------------
- Tkinter is a built-in Python library that lets you create graphical user interfaces (GUIs).
- A GUI program lets users click buttons, type in text boxes, and see drawings rather than only working with text.
- When using Tkinter, you create a window and add "widgets" (labels, buttons, etc.) to that window.

Example: Your First Tkinter Window
------------------------------------
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Tkinter Window")
root.geometry("400x300")  # 400 pixels wide, 300 pixels high

# Create a label (a piece of text)
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)  # pady adds vertical space

# Create a button to close the window
close_button = tk.Button(root, text="Close", command=root.destroy)
close_button.pack()

# Start the event loop
root.mainloop()

What to Notice:
- The window has a title and a set size.
- The label shows a message.
- The button closes the window.
- root.mainloop() starts the program, waiting for events.

-------------------------------------------------------------------------------
2. Lesson 5: Animated Area Calculator
-------------------------------------------------------------------------------
Objective:
- Build a GUI where you pick a shape, enter its size(s), calculate its area, and see the shape animate on the screen.

A. Setup and Imports
----------------------
import tkinter as tk
from tkinter import ttk, messagebox
import time
from math import cos, sin, pi

Notes:
- ttk gives a nicer look.
- messagebox shows popup error messages.
- time is used for creating pauses (animation).
- math functions help draw shapes like pentagons.

B. Calculating the Area
--------------------------
A function to calculate the area based on the selected shape:

def calculate_area():
    shape = shape_var.get()  # Get the shape from the drop-down list
    try:
        if shape == "Circle":
            radius = float(entry1.get())
            area = 3.14159 * radius * radius
        elif shape == "Square":
            side = float(entry1.get())
            area = side * side
        # You can add more formulas for Rectangle, Triangle, etc.
        else:
            messagebox.showerror("Error", "Please select a shape")
            return
      
        result_var.set(f"Area: {area:.2f}")  # Display area rounded to 2 decimals
        draw_shape(shape, area)  # Animate drawing the shape
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

C. Dynamic UI for Dimensions
-------------------------------
Some shapes (like Rectangles and Triangles) need two dimensions. This function shows a second input when needed:

def update_fields(*args):
    shape = shape_var.get()
    if shape == "Rectangle" or shape == "Triangle":
        label2.grid(row=2, column=0)
        entry2.grid(row=2, column=1)
    else:
        label2.grid_forget()
        entry2.grid_forget()

shape_var.trace("w", update_fields)

D. Drawing and Animating the Shape
--------------------------------------
We use a Canvas to draw. Here’s how to animate a circle:
 
def animate_circle(x, y, r, color, original_radius):
    steps = 100  # Number of steps in the animation
    for i in range(steps + 1):
        canvas.delete("all")  # Clear the canvas at each step
        radius = r * i / steps  # Increase radius gradually
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
        canvas.update()
        time.sleep(0.01)  # Wait 0.01 seconds between steps
    canvas.create_text(x, y + r + 20, text=f"Radius = {original_radius}", fill="black")

E. Complete GUI Setup
------------------------
The full program includes:
- Input fields for dimensions.
- A drop-down list for shape selection.
- A button to calculate the area.
- A canvas where shapes are animated.

-------------------------------------------------------------------------------
3. Lesson 6: Simple Pong Game
-------------------------------------------------------------------------------
Objective:
- Create a game window with a black background.
- Draw and animate paddles and a bouncing ball.
- Use keyboard input to move the paddles.

A. Game Window and Canvas
----------------------------
import tkinter as tk

root = tk.Tk()
root.title("Pong Game")
canvas = tk.Canvas(root, width=800, height=400, bg="black")
canvas.pack()

B. Drawing the Paddles and Ball
---------------------------------
paddle1 = canvas.create_rectangle(30, 150, 50, 250, fill="white")
paddle2 = canvas.create_rectangle(750, 150, 770, 250, fill="white")
ball = canvas.create_oval(390, 190, 410, 210, fill="white")

C. Animating the Ball
------------------------
Variables control the ball's speed:
ball_dx = 3  # Horizontal speed
ball_dy = 3  # Vertical speed

def move_ball():
    global ball_dx, ball_dy
    canvas.move(ball, ball_dx, ball_dy)
    ball_pos = canvas.coords(ball)  # Get ball coordinates [x1, y1, x2, y2]
    
    # Bounce off the top and bottom edges
    if ball_pos[1] <= 0 or ball_pos[3] >= 400:
        ball_dy = -ball_dy
    # Bounce off the left and right edges
    if ball_pos[0] <= 0 or ball_pos[2] >= 800:
        ball_dx = -ball_dx
    
    root.after(50, move_ball)  # Repeat the function after 50ms

move_ball()

D. Moving the Paddles with Keyboard
-----------------------------------------
def move_paddle(event):
    if event.keysym == "w":
        canvas.move(paddle1, 0, -20)
    elif event.keysym == "s":
        canvas.move(paddle1, 0, 20)
    elif event.keysym == "Up":
        canvas.move(paddle2, 0, -20)
    elif event.keysym == "Down":
        canvas.move(paddle2, 0, 20)

canvas.bind_all("<KeyPress>", move_paddle)

Try pressing “w”, “s”, “Up”, and “Down” to control the paddles!

-------------------------------------------------------------------------------
4. Lesson 7: To-Do List Application
-------------------------------------------------------------------------------
Objective:
- Build a simple application to manage tasks.
- Learn to add, remove, and mark tasks as completed.
- Update the screen using a Listbox widget.

A. Setup and GUI Layout
---------------------------
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x400")

B. Task Management Functions
------------------------------
We use two lists: one for tasks and one for their completion status.
tasks = []
completed_status = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        completed_status.append(False)  # Task is not completed initially
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        del completed_status[selected_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove.")

def mark_task_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        completed_status[selected_index] = True
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as completed.")

C. Building and Updating the List Display
----------------------------------------------
def update_listbox():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "(completed)" if completed_status[i] else "(uncompleted)"
        task_listbox.insert(tk.END, f"{i+1}. {task} {status}")

# Create the Entry box to add new tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons for adding, removing, and marking tasks
tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Remove Task", command=remove_task).pack()
tk.Button(root, text="Mark Task as Completed", command=mark_task_completed).pack()

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

root.mainloop()

Test it out by adding, removing, and marking tasks!

-------------------------------------------------------------------------------
5. Final Thoughts
-------------------------------------------------------------------------------
- Tkinter lets you create fun, interactive windows.
- Experiment with code: change colors, speeds, shapes, and sizes.
- Ask questions if something isn’t clear—learning by doing is the best way to understand!

Happy Coding!
=================================================

