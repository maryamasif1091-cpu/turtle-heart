import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)         # Animated speed (1 = slow, 3 = medium, 6 = fast)
t.hideturtle()
t.pensize(1)

colors = ["red", "orange", "yellow", "green", "cyan", "lime", "purple", "pink"]

for i in range(120):
    # Center position 
    t.penup()
    t.goto(0, 40)
    
    # Mathematical heart formula
    angle = i * (math.pi * 2) / 120
    x = 16 * (math.sin(angle) ** 3) * 15
    y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * 15
    
    # Line draw till heart boundary
    c = random.choice(colors)
    t.color(c)
    t.pendown()
    t.goto(x, y)
    
    # End point star pattern
    for _ in range(8):
        t.forward(5)
        t.backward(5)
        t.right(45)

turtle.done()