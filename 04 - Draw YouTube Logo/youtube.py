import turtle

t = turtle.Turtle()

turtle.bgcolor('black')
t.color('white')
t.hideturtle()
t.fillcolor('red')
t.begin_fill()

for i in [300, 200] * 2:
    t.forward(i)
    t.circle(30, 90)

t.end_fill()
t.penup()
t.goto(120, 80)
t.pendown()
t.fillcolor("white")
t.begin_fill()

for i in [30, 120, 120]:
    t.left(i)
    t.forward(100)

t.end_fill()
turtle.done()