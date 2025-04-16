import random
import turtle
import time
import math

t = turtle.Turtle()
ask_explosion = int(input("Enter Number. 1 = fiery blast, 2 = star blaster, 5 = tree, 7 = this is so boring EXIT, 6 = some math: "))
print("Starting your choice")
time.sleep(2)
if ask_explosion == 1:
    t.penup()
    t.left(90)
    t.forward(250)
    t.pendown()
    t.speed(3)
    t.pencolor('red')
    t.fillcolor('black')
    t.begin_fill()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.end_fill()
    time.sleep(1)
    t.left(90)
    t.penup()
    t.forward(100)
    t.pendown()
    t.pensize(5)
    t.forward(300)
    for _ in range(random.randint(50, 100)):
        t.speed(0)
        random_size = random.randint(1, 50)
        fire = ["red", "orange", "yellow"]
        fire_color = random.choice(fire)
        t.pencolor(fire_color)
        t.fillcolor(fire_color)
        t.begin_fill()
        t.circle(random_size)
        t.end_fill()
        t.goto(random.randint(-60, 60), random.randint(-70, 70))
        t.end_fill()
if ask_explosion == 2:
    t.penup()
    t.left(90)
    t.forward(250)
    t.pendown()
    t.speed(3)
    t.pencolor('red')
    t.fillcolor('black')
    t.begin_fill()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.end_fill()
    t.left(90)
    t.penup()
    t.forward(100)
    t.pendown()
    t.pensize(5)
    t.forward(300)
    color_list = ['red', 'orange', 'yellow', 'green', 'purple', 'blue']
    colorssss = random.choice(color_list)
    t.speed(0)
    for _ in range(10):
        for _ in range(10):
            t.fillcolor(colorssss)
            t.begin_fill()
            t.forward(100) 
            t.right(144+10)
            t.end_fill()
            t.penup()
            t.goto(random.randint(-100, 100))
            t.pendown()
if ask_explosion == 5:
    
    t.speed(0)
    
    def draw_tree(branch_length):
        t.pensize(3)
        t.pencolor('brown')
        if branch_length > 5:  # Base case: stop recursion when branch length is too short
            t.forward(branch_length)  # Draw the current branch
            t.right(20)  # Turn right to draw the right subtree
            draw_tree(branch_length - 15)  # Recursively draw the right subtree with shorter branches
            t.left(40)  # Turn left to draw the left subtree
            draw_tree(branch_length - 15)  # Recursively draw the left subtree with shorter branches
            t.right(20)  # Restore the original orientation
            t.backward(branch_length)  # Move the turtle back to the starting point of the branch
    draw_tree(100)
    t.penup()
    t.forward(300)
    t.pendown()
    for _ in range(100):
        circlek = random.randint(1, 50)
        t.pencolor('green')
        t.fillcolor('green')
        t.begin_fill()
        t.circle(circlek)
        t.left(random.randint(-60, 60))
        t.forward(5)
        t.end_fill()
        t.left(90)
        t.forward(80)
        t.left(180)
if ask_explosion == 6:
    printing = int(input("Enter number for sqaure root")
    print(math.sqrt(printing))
if ask_explosion == 7:
    pass
turtle.done()
