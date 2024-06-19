import turtle as t
import random

race_on = False
screen = t.Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="make your bet", prompt="who will win the race?")
colour = ['red','green','yellow','blue','purple','orange']
y = [-70,-40,-10,20,50,80]
all_turtle = []


for turtle_count in range(0,6):
    new_turtle = t.Turtle(shape ='turtle')
    new_turtle.penup()
    new_turtle.color(colour[turtle_count])
    new_turtle.goto(x=-230, y=y[turtle_count])
    all_turtle.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'you have won. the {winning_color} is the winner!')
            else:
                print(f'you have lost. the {winning_color} is the winner!')
        rand_dis = random.randint(0,10)
        turtle.forward(rand_dis)
        turtle.speed(random.randint(1,15))

screen.exitonclick()