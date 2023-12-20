from turtle import Turtle, Screen
import random

finish = False
screen = Screen()
width = 780
screen.setup(width, 400)

bet = screen.textinput("Bet", "Make a bet:")

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
coord = [125, 75, 25, -25, -75, -125]
turtles = []

for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-1 * ((width - 25) / 2), coord[i])
    turtles.append(new_turtle)

while not finish:
    for turtle in turtles:
        speed = random.randint(0, 10)
        turtle.forward(speed)
        if turtle.xcor() >= ((width - 25) / 2):
            finish = True
            winner = turtle.color()[0]
            print(f"Winner is {winner}.")
            if bet == winner:
                print("You win.")
            else:
                print("You lose.")
                break

screen.exitonclick()
