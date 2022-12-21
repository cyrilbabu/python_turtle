import turtle
import random

s = turtle.Screen()
t = turtle.Turtle()
t.speed("fastest")
turtle.colormode(255)

def randam_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for i in range(36+36):
    t.color(randam_color())
    t.circle(100)
    t.left(5)

s.exitonclick()