import colorgram
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


def extract_color(number_of_colors):
    color = []
    colors = colorgram.extract('image.jpg', number_of_colors)
    for j in range(number_of_colors):
        rbg = []
        for i in range(3):
            first_color = colors[j].rgb[i]
            rbg += [first_color]
            rgb = tuple(rbg)
        color.append(rgb)
    return color


def print_dots(row, column , colors, pen_size):
    t.pensize(pen_size)
    t.penup()
    t.back(((pen_size*2)*row + row)//2)
    t.right(90)
    t.forward(((pen_size*2)*column)//2)
    t.left(90)
    t.pendown()
    for i in range(column):
        for j in range(row):
            t.color(randam_color())
            t.forward(1)
            t.penup()
            t.forward((pen_size*2))
            t.pendown()
        t.penup()
        t.left(90)
        t.forward((pen_size*2))
        t.right(90)
        t.back((pen_size*2)*row + row)
        t.pendown()


row = int(s.textinput(title="row",prompt="number of row:  "))
column = int(s.textinput(title="column",prompt="number of column:  "))
pen_size = int(s.textinput(title="pen_size",prompt="number of pen_size:  "))
colors = extract_color(column)
print_dots(row, column, colors, pen_size)

s.exitonclick()
