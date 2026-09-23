###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle
import random as rand

rgb_colors = []
colors = colorgram.extract(r'UdemyCourse\Day18\Hirst\image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

print(rgb_colors)

t = turtle.Turtle()
turtle.colormode(255)
t.speed(1)
s = turtle.Screen()
for i in range(10):
    t.penup()
    t.right(5)
    t.goto(0,0)
    for j in range(10):
        t.pendown()
        t.forward(10)
        t.dot(10,rand.choice(rgb_colors))
s.exitonclick()