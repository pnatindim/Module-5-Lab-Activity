#Patric Natindim
#March 5 2025

#Draws a polygon based on the dimensions and colors you give it

import turtle

sides = int(input("Number of sides: "))
length = int(input("Length of each side: "))
line_color = input("Color of the line: ")
fill_color = input("Fill color: ")

screen = turtle.Screen()
t = turtle.Turtle()

t.pencolor(line_color)
t.fillcolor(fill_color)

t.begin_fill()

for _ in range(sides):
    t.forward(length)
    t.left(360 / sides)  

t.end_fill()

t.hideturtle()

screen.mainloop()
