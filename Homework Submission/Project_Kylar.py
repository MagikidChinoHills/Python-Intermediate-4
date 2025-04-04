import random
import turtle
import math
t = turtle.Turtle()
t.penup()
t.backward(180)
t.pendown()
cnc = random.randint(100, 20000)
for _ in range(cnc):
  t.speed(0)
  svh = ["red", "yellow", "orange", "blue", "purple", "green"]
  poop = random.choice(svh)
  t.pencolor('white')
  diahrea_mixer = random.randint(1, 100)
  t.fillcolor(poop)
  t.begin_fill()
  t.forward(diahrea_mixer)
  t.left(diahrea_mixer)
  t.circle(diahrea_mixer)
  t.forward(diahrea_mixer - 70)
  t.left(diahrea_mixer)
  hi = math.sin(45)
  hello = math.radians(hi)
  t.circle(diahrea_mixer - hello)
  t.end_fill()
  if t == 5:
      t.circle(random.randint(1, 90))
turtle.done()
t.fillcolor("black")
t.begin_fill()
t.circle(5)
t.end_fill()
print("Done")
