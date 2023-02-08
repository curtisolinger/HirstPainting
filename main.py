import turtle
import hirst_colors
import random

sam = turtle.Turtle()
sam.shape("turtle")
turtle.colormode(255)
sam.speed("fastest")
sam.hideturtle()
sam.penup()
y_position = -250

def draw_a_dot(size):
    sam.pendown()
    sam.dot(size, random.choice(hirst_colors.colors))
    sam.penup()

for _ in range(10):
    sam.goto(-250, y_position)
    for _ in range(10):
        draw_a_dot(20)
        sam.forward(50)
    y_position += 50

screen = turtle.Screen()
screen.exitonclick()
