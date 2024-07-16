# By : Youssef Tharwat

import turtle

t = turtle.Turtle()

turtle.bgcolor("#ffffff")
t.color("#f3ab04")


# Create a rectangle..
def rect():
    t.pensize(9)
    t.forward(170)
    t.left(45)
    t.forward(6)
    t.left(45)
    t.forward(170)
    t.left(45)
    t.forward(6)
    t.left(45)
    t.forward(330)
    t.left(45)
    t.forward(6)
    t.left(45)
    t.forward(170)
    t.left(45)
    t.forward(6)
    t.left(45)
    t.forward(170)


# create a function to drawing the four corners lines left to right
def four_corner_lines():
    t.pensize(12)
    t.penup()
    t.forward(180)
    t.left(90)
    t.forward(35)
    t.left(90)
    t.pendown()
    t.forward(12)
    t.penup()
    t.forward(344)
    t.pendown()
    t.forward(17)
    t.penup()
    t.right(90)
    t.forward(105)
    t.right(90)
    t.pendown()
    t.forward(17)
    t.penup()
    t.forward(344)
    t.pendown()
    t.forward(12)


# Drawing the P...
def p():
    t.penup()
    t.left(180)
    t.forward(280)
    t.pendown()
    t.forward(40)
    t.left(90)
    t.forward(100)
    t.left(180)
    t.forward(52)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(47)


# Drawing the U...
def u():
    t.penup()
    t.right(90)
    t.forward(32)
    t.right(90)
    t.pendown()
    t.forward(98)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(98)


# Drawing the B..
def b():
    t.penup()
    t.right(90)
    t.forward(35)
    t.pendown()
    t.forward(45)
    t.right(90)
    t.forward(43)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(40)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(40)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(40)
    t.right(90)
    t.forward(45)
    t.right(90)
    t.forward(96)


# Drawing the G..
def g():
    t.penup()
    t.right(180)
    t.forward(53)
    t.left(90)
    t.forward(90)
    t.pendown()
    t.forward(25)
    t.right(90)
    t.forward(45)
    t.right(90)
    t.forward(45)
    t.right(90)
    t.forward(95)
    t.right(90)
    t.forward(40)


# calling the rect() function...
rect()
# calling the four_corner_lines() function..
four_corner_lines()
# calling the p(), u(), b(), g() functions..
p()
u()
b()
g()

t.penup()
t.goto(-213,-160)
t.pendown()
t.pencolor("#f3ab04")
t.write("PUBG Mobile", font=("klavika",50, "bold"))

turtle.done()
