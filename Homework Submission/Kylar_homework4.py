# problem 1, Hexagon with color
import turtle
t = turtle.Turtle()
t.fillcolor('red')
t.begin_fill()
for _ in range(6):
	t.forward(80)
	t.right(60)
t.end_fill()
turtle.done()

# Problem 2, Mandala Design
import turtle

t = turtle.Turtle()
t.speed(0)
t.circle(49)
t.penup()
t.right(175)
t.forward(4)
t.pendown()

t.circle(59)
t.penup()
t.right(175)
t.forward(4)
t.pendown()
t.penup()
t.left(-100)
t.forward(120)
t.right(85)
t.pendown()

t.circle(69)
t.penup()
t.right(175)
t.forward(4)
t.pendown()
t.penup()
t.left(-100)
t.forward(138)
# And so on...

# Problem 3, Spinning Triangle
import time
import turtle

t = turtle.Turtle()

for _ in range(90):
	for _ in range(2):
  	t.forward(80)
  	t.left(120)
	t.forward(80)
turtle.done()

# Problem 4, Nested sqaures
import turtle

t = turtle.Turtle()
t.speed(0)
for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.left(180)

for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(80)
for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(-870)

for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(80)
for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(-870)

for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(80)
for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(-870)

for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(80)
for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(-870)

for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(80)
for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(-870)

for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(80)
for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(-870)

for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(80)
for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(-870)

for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(80)
for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(-870)

for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(80)
for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(-870)

for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(80)
for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(-870)

for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(80)
for _ in range(4):
  increase = (10) + 10
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 20
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 30
  t.forward(increase)
  t.left(90)
for _ in range(4):
  increase = (10) + 40
  t.forward(increase)
  t.left(90)
t.right(-870)
turtle.done()
