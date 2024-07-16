import turtle

t = turtle.Turtle()

turtle.bgcolor("Black")
t.pensize(3)
t.speed(0)

for i in range(400):
    for colors in("red", "gold", "purple", "deeppink", "lime"):
        t.color(colors)
        t.circle(100)
        t.left(200)

turtle.done()