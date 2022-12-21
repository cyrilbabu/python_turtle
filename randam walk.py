import turtle
import random

def ramdaom_turtle(t):
    t.pensize(random.choice(pen))
    t.color(randam_color())
    t.forward(random.choice(step))
    t.right(random.choice(angle))


s = turtle.Screen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t1.speed("fastest")
t2.speed("fastest")
t3.speed("fastest")
t4.speed("fastest")
t5.speed("fastest")

turtle.colormode(255)

def randam_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


angle = [0, 90, 90, 180, 270, 270]
step = [20, 25, 35]
pen = [5, 10, 0, 7]

while True:
    s.bgcolor(randam_color())
    ramdaom_turtle(t1)
    ramdaom_turtle(t2)
    ramdaom_turtle(t3)
    ramdaom_turtle(t4)
    ramdaom_turtle(t5)

s.exitonclick()
