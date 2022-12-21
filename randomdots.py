import turtle
import random
import colorgram

s = turtle.Screen()
t = turtle.Turtle()
t.speed("fastest")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
