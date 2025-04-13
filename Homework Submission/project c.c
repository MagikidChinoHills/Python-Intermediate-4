1
import turtle
import random

tool = turtle.Turtle()
tool.begin_fill()
tool.fillcolor('black')
for _ in range(2):
    tool.forward(150)
    tool.left(360/4)
    tool.forward(75)
    tool.left(360/4)


tool.end_fill()



tool.penup
tool.goto(0, 75)
tool.pendown

tool.fillcolor('red')
tool.begin_fill()
for _ in range(2):
    tool.forward(25)
    tool.left(360/4)
    tool.forward(35)
    tool.left(360/4)

tool.end_fill()

tool.penup
tool.goto(65, 10)
tool.pendown

tool.fillcolor('blue')
tool.begin_fill()
for _ in range(2):
    tool.forward(50)
    tool.left(360/4)
    tool.forward(50)
    tool.left(360/4)


tool.end_fill()

tool.penup
tool.goto(10, 0)
tool.pendown

tool.fillcolor('white')
tool.begin_fill()
for _ in range(2):
    tool.forward(20)
    tool.left(360/4)
    tool.forward(40)
    tool.left(360/4)


tool.end_fill()

tool.penup
tool.goto(66, 75)
tool.pendown


def draw_tree(branch_length):
    if branch_length > 5: 
        tool.forward(branch_length) 
        tool.right(20)  
        draw_tree(branch_length - 15)  
        tool.left(40)  
        draw_tree(branch_length - 15) 
        tool.right(20) 
        tool.backward(branch_length)  


tool.left(90) 
tool.penup()  
tool.goto(0, -200) 
tool.pendown() 
draw_tree(100)


for _ in range(5):
    tool.penup
    x = random.randint(-360, 360)
    x = random.randint(150, 360)
    tool.goto(x, y)
    tool.pendown
    for _ in range(2):
        tool.forward(50)
        tool.left(360/4)
        tool.forward(50)
        tool.left(360/4)
    

turtle.done()



