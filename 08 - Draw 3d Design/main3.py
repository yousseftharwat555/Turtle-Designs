import turtle

turtle.bgcolor("Black")
turtle.pensize(3)
turtle.speed(0)

for i in range(15):
    turtle.color("red")
    turtle.circle(100)
    turtle.left(10)
    turtle.forward(i)
    turtle.circle(100)
    turtle.left(90)

turtle.done()