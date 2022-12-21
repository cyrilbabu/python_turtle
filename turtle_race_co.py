import random
from turtle import Turtle, Screen

s = Screen()
s.setup(width=500, height=500)
user_bet = s.textinput(title="place your bet", prompt="which turtle will win")
colors = ["red", "blue", "yellow", "orange", "green", "purple"]
y_axis = [125, 75, 25, -25, -75, -125]
all_turtles = []

game = False
if user_bet:
    game = True

for i in range(6):
    tim = Turtle()
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_axis[i])
    all_turtles.append(tim)

print(all_turtles)

while game:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game = False
            wining = turtle.pencolor()
            if wining == user_bet:
                print(f"you won {wining}")
            else:
                print(f"you loss {wining}")

        step = random.randint(1, 10)
        turtle.forward(step)

s.exitonclick()
