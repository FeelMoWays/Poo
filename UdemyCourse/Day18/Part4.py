import turtle
import random as rand 
t = turtle.Turtle()
turtle.colormode(255)
t.speed(1)
s = turtle.Screen()
def random_color():
    r = rand.randint(0,255)
    g = rand.randint(0,255)
    b = rand.randint(0,255)
    color = (r,g,b)
    return color
for i in range(100):
    t.speed(100)
    t.circle(100)
    t.pencolor(random_color())
    t.right(2)
s.exitonclick()