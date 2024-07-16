import turtle

turtle.bgcolor("black")
turtle.pensize(3)
turtle.speed(0)

for i in range(400):
    for colors in('red', 'deeppink', 'lime', 'purple'):
        turtle.color(colors)
        turtle.left(100)
        turtle.circle(100)

turtle.done()