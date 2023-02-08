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
        sam.color(sam_color)
        sam.fillcolor(sam_color)
        sam.begin_fill()
        sam.circle(10)
        sam.end_fill()
        sam.penup()
        sam.forward(50)
    y_position += 50



screen = turtle.Screen()
screen.exitonclick()
