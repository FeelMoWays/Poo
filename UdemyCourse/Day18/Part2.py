from turtle import Turtle,Screen
t = Turtle()
t.speed(1)
s = Screen()
for i in range(10):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
s.exitonclick()