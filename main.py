from turtle import Turtle, Screen, color
import turtle
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title="Place Your Bet", prompt= "Which turtle will win the race? Pick a oolour from the ROYGBV Rainbow: ")
print(user_bet)

all_turtles = []

rob = Turtle(shape ="turtle")
rob.color("red")
rob.penup()
rob.goto(x = -240, y=-100)
all_turtles.append(rob)

ollie = Turtle(shape = "turtle")
ollie.color("orange")
ollie.penup()
ollie.goto(x= -240, y = -50)
all_turtles.append(ollie)

yuki = Turtle(shape = "turtle")
yuki.color("yellow")
yuki.penup()
yuki.goto(x= -240, y = 0)
all_turtles.append(yuki)

giles = Turtle(shape = "turtle")
giles.color("green")
giles.penup()
giles.goto(x= -240, y = 50)
all_turtles.append(giles)

bob = Turtle(shape = "turtle")
bob.color("blue")
bob.penup()
bob.goto(x= -240, y = 100)
all_turtles.append(bob)

viv = Turtle(shape = "turtle")
viv.color("violet")
viv.penup()
viv.goto(x= -240, y = 150)
all_turtles.append(viv)



if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won. The winner is {winning_colour} ")
            else: 
                print(f"You've lost. The winner is {winning_colour} ")

        rand_distance = random.randint(1,11)
        turtle.forward(rand_distance)


screen.exitonclick()