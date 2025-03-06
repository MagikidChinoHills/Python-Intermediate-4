#problem 1
import turtle
import random

t = turtle.Turtle

for _ in range(5):
    poop = random.randint(0, 360)
    t.forward(30)
    t.right(poop)
    
#problem 2
import turtle as t
import random as r
for _ in range(100):
    random = ['red', 'yellow', 'blue', 'green', 'purple', 'silver']
    t.forward(100)
    t.left(70)
    t.pencolor(r.choice(random))
turtle.done()
#problem 3
import turtle as t
import random
t.speed(0)
def draw_sgraph(size):
    for _ in range(int(36000000000000000000000000000000 / size)):#You could change the number 360 to make it longer or shorter
        t.pencolor(random.choice(['red', 'green', 'yellow', 'blue', 'orange', 'gray', 'purple']))
        t.circle(100)
        t.right(size)
draw_spirograph(1)
turtle.done()
#problem 4
import turtle as t
import random
t.speed(0)
def draw_spirograph(size):
    for _ in range(int(360 / size)):#You could change the number 360 to make it longer or shorter
        t.pencolor(random.choice(['red', 'green', 'yellow', 'blue', 'orange', 'gray', 'purple']))
        t.circle(100)
        t.right(size)
draw_spirograph(100)
turtle.done()
                

#problem 5
import turtle as t
import random
t.speed(0)
def draw_spirograph(size):
    for _ in range(int(360 / size)):#You could change the number 360 to make it longer or shorter
        randompoop = random.randint[1, 100]
        t.pencolor(random.choice(['red', 'green', 'yellow', 'blue', 'orange', 'gray', 'purple']))
        t.circle(randompoop)
        t.right(size)
draw_spirograph(1)
turtle.done()
                
#Kylar.done
