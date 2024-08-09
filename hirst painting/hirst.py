# # to extract the rgb of colours in an image
# import colorgram
# rgb_color = []
# colors = colorgram.extract('hirst.jpeg', 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)

import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
colours = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    tim.dot(20, random.choice(colours))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()


