import turtle

turtle.bgcolor("black")
turtle.speed(0)
turtle.pensize(3)

for i in range(200):
    for colors in ('deeppink', 'lime', 'red'):
        turtle.color(colors)
        turtle.circle(100-i)
        turtle.left(20)

turtle.done()