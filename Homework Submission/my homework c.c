1
import turtle

tool = turtle.Turtle()

  for _ in range(2):
    tool.forward(150)
    tool.left(360/4)
    tool.forward(75)
turtle.done()


2
  
import turtle

tool = turtle.Turtle()

  for _ in range(6):
    tool.forward(80)
    tool.left(360/6)

turtle.done()



  
3

import turtle

tool = turtle.Turtle()

tool.fillcolor("red")
tool.pencolor("black")
tool.begin_fill()

def draw_star(side,length):
  for _ in range(side):
    tool.forward(length)
    tool.left(360/side)

draw_star(5, 100)

tool.end_fill()

turtle.done()


 5 

import turtle

tool = turtle.Turtle()

tool.fillcolor("yellow")
tool.pencolor("black")
tool.begin_fill()

def draw_polygon(side,length):
  for _ in range(side):
    tool.forward(length)
    tool.left(360/side)

draw_polygon(100, 5)

tool.end_fill()

turtle.done()
