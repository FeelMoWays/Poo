from turtle import Turtle,Screen
t = Turtle()
t.speed(1)
s = Screen()
def shape(sides):
    angles = 360/sides
    for i in range(sides):
        t.forward(10)
        t.right(angles)

shape(15)
s.exitonclick()
