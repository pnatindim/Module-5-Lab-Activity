# Patric Natindim
# March 5 2025

# Draws a house

import turtle

screen = turtle.Screen()

t = turtle.Turtle()
t.speed(3)

# Foundation
t.penup()
t.goto(-100, -100)
t.pendown()
t.begin_fill()
t.fillcolor("yellow")
for _ in range(2):
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()

# Roof
t.penup()
t.goto(-120, 100)
t.pendown()
t.begin_fill()
t.fillcolor("brown")
for _ in range(3):
    t.forward(240)
    t.left(120)
t.end_fill()

# Door
t.penup()
t.goto(-25, -100)
t.pendown()
t.begin_fill()
t.fillcolor("brown")
for _ in range(2):
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()

#Window
t.penup()
t.goto(50, 50)
t.pendown()
t.begin_fill()
t.fillcolor("light blue")
for _ in range(4):
    t.forward(50)
    t.left(90)
t.end_fill()

t.hideturtle()

screen.mainloop()
