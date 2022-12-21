import turtle
import random

s = turtle.Screen()
tj = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()

step = [5, 1, 10, 1, 5, 1, 10, 1, 15, 1, 5, 1, 10, 1, 15, 1, 20, 1, 5, 1, 10, 1, 5, 1, 10,50 ,1, 15, 1, 5, 1, 10, 1, 15, 1, 20, 1, 5, 1, 10, 1, 5, 1, 10, 1, 15, 1, 5, 1, 10, 1, 15, 1, 20, 1, 5, 1, 10, 1, 5, 1, 10, 1, 15, 1, 5, 1, 10, 1, 15, 1, 20, 1]

def starting_line():
    t1.shape("turtle")
    t2.shape("turtle")
    t3.shape("turtle")
    t4.shape("turtle")
    t5.shape("turtle")

    t1.color("red")
    t2.color("green")
    t3.color("pink")
    t4.color("blue")
    t5.color("purple")

    t1.speed("fastest")
    t2.speed("fastest")
    t3.speed("fastest")
    t4.speed("fastest")
    t5.speed("fastest")
    tj.speed("fastest")

    tj.isvisible()
    tj.penup()
    tj.forward(400)
    tj.pendown()
    tj.left(90)
    tj.forward(150)
    tj.back(300)

    t1.penup()
    t2.penup()
    t3.penup()
    t4.penup()
    t5.penup()

    t1.back(400)

    t2.left(90)
    t2.forward(50)
    t2.right(90)
    t2.back(400)

    t3.right(90)
    t3.forward(50)
    t3.left(90)
    t3.back(400)

    t4.right(90)
    t4.forward(100)
    t4.left(90)
    t4.back(400)

    t5.left(90)
    t5.forward(100)
    t5.right(90)
    t5.back(400)

    t1.pendown()
    t2.pendown()
    t3.pendown()
    t4.pendown()
    t5.pendown()


def turtle_move(t):
    print()
    global game
    global finesh1
    global finesh2
    global finesh3
    global finesh4
    global finesh5

    if finesh1 < 800 and finesh2 < 800 and finesh3 < 800 and finesh4 < 800 and finesh5 < 800:
        move = random.choice(step)
        t.forward(move)
        if t == t1:
            finesh1 += move
        elif t == t2:
            finesh2 += move
        elif t == t3:
            finesh3 += move
        elif t == t4:
            finesh4 += move
        else:
            finesh5 += move
    else:
        game = False

game = True

starting_line()
finesh1 = 0
finesh2 = 0
finesh3 = 0
finesh4 = 0
finesh5 = 0

t1.speed("slowest")
t2.speed("slowest")
t3.speed("slowest")
t4.speed("slowest")
t5.speed("slowest")
tj.speed("slowest")

while game:
    turtle_move(t1)
    turtle_move(t2)
    turtle_move(t3)
    turtle_move(t4)
    turtle_move(t5)

if finesh1 > 800:
    print("red is winer")
elif finesh2 > 800:
    print("green is winer")
elif finesh3 > 800:
    print("pink is winer")
elif finesh4 > 800:
    print("blue is winer")
elif finesh5 > 800:
    print("purple is winer")



s.exitonclick()