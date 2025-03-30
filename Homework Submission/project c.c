1
import turtle

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
turtle.done()



