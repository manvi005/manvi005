import turtle as t
import random
timmy = t.Turtle()
t.colormode(255)

# for a dashed lne

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# for all shapes together

# def shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for sides in range(3, 11):
#     timmy.color(random.choice(colours))
#     shape(sides)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

#  for lines in random direction and color

# directions = [0,90,180.270]
# timmy.pensize(10)
timmy.speed(15)
#
# for _ in range(200):
#     timmy.color(random_colour())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))


# for spiral effect of circle

# def spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         timmy.color(random_colour())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)
#
#
# spirograph(5)

screen = t.Screen()
screen.exitonclick()

