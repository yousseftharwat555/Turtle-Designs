# By : Youssef Tharwat

from turtle import *
import turtle

t = turtle.Turtle()
t.color("yellow")


bgcolor("yellow")

width(20)
penup()
goto(100,100)
pendown()
fillcolor("white")
begin_fill()
setheading(90)
circle(100,180)
fd(30)
lt(-110)
fd(30)
circle(25,180)
fd(20)
setheading(85)
circle(140,-60)
lt(-65)
circle(250,13)
lt(-70)
fd(15)
lt(90)
fd(52)
setheading(-28)
circle(198,54)
setheading(0)
fd(52)
lt(90)
fd(15)
lt(-70)
circle(250,13)
lt(-65)
circle(140,-60)
setheading(5)
fd(30)
circle(25,180)
fd(30)
lt(-90)
fd(30)
end_fill()

up()
goto(-19.0,-232.0)
down()

color('black')


t.penup()
t.goto(-150,-260)
t.pendown()
t.pencolor("black")
t.write("SnapChat", font=("klavika",50, "bold"))

done()