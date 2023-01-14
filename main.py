# import colorgram
#
# colors = colorgram.extract("image.jpg", 40)
# color_array = []
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     color_array.append((r, g, b))
# print(color_array)

from turtle import  Turtle, Screen
import random as r

turtle = Turtle()
screen = Screen()
color_list = [(244, 235, 46), (196, 12, 34), (221, 159, 69), (43, 80, 178), (238, 39, 143), (40, 215, 68), (238, 229, 5), (30, 40, 154), (23, 147, 26), (207, 74, 22), (202, 34, 91), (186, 16, 9), (19, 18, 42), (216, 141, 191), (57, 15, 10), (88, 8, 28), (227, 161, 9), (78, 212, 157), (67, 73, 221), (13, 95, 61), (78, 194, 225), (239, 158, 215), (94, 233, 204), (220, 76, 48), (15, 67, 46), (7, 226, 238), (100, 226, 236), (243, 164, 155), (170, 175, 240), (252, 6, 60), (5, 245, 224)]

turtle.shape("arrow")
turtle.speed("fastest")
screen.colormode(255)
turtle.penup()
turtle.setx(-200)
turtle.sety(-200)
print(turtle.pos())
turtle.hideturtle()


def draw_dots_lined(columns=10, size=20, distance=50):
    for i in range(columns):
        turtle.pendown()
        turtle.dot(size, r.choice(color_list))
        turtle.penup()
        turtle.forward(distance)


def move_up(columns=10, distance=50):
    turtle.back(columns*distance)
    turtle.setheading(90)
    turtle.forward(distance)
    turtle.setheading(0)


def draw_hirst(columns=10, size=20, distance=50):
    for i in range(columns):
        draw_dots_lined(columns=columns, size=size, distance=distance)
        move_up(columns=columns)


draw_hirst()
screen.exitonclick()

