import turtle
import colorsys as cs

turtle.speed(0)
turtle.bgcolor("black")
turtle.pensize(3)
turtle.pencolor("red")

for i in range(200):
    for j in range(50):
        turtle.color(cs.hsv_to_rgb(i/15, j/50, 1))
        turtle.left(500)
        turtle.circle(i-120, 97)
        turtle.right(300)

turtle.hideturtle()
turtle.done()