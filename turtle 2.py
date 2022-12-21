import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.speed(1)

color = ["red", "pink", "blue", "green", "black", "purple", "orange"]

for i in range(3, 10):
    t.color(color[i - 4])
    for j in range(i):
        t.forward(100)
        t.right(360/i)

s.exitonclick()
