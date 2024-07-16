# By : Youssef Tharwat

from turtle import *
import turtle

t = turtle.Turtle()
t.color("#f3f3f3")


bgcolor('#f3f3f3')
pencolor('deeppink')
width(23)
penup()
goto(160,-100)
pendown()

left(90)
for i in range(4):
 forward(250)
 circle(34,90)

penup()
goto(85,30)
pendown()
circle(80,360)
penup()
goto(110,130)
pendown()
circle(7,360)
hideturtle()

t.penup()
t.goto(-150,-260)
t.pendown()
t.pencolor("deeppink")
t.write("Instagram", font=("klavika",50, "bold"))

done()
