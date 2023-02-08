import turtle
import hirst_colors
import random

sam = turtle.Turtle()
sam.shape("turtle")
turtle.colormode(255)
sam.speed("fastest")

y_position = -250

for i in range(10):
    sam.penup()
    sam.goto(-250, y_position)
    for j in range(10):
        sam_color = random.choice(hirst_colors.colors)
        sam.pendown()
        sam.dot(20, sam_color)
        sam.penup()
        sam.forward(50)
    y_position += 50



screen = turtle.Screen()
screen.exitonclick()
