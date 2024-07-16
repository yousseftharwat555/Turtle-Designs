import turtle as t

# set up the turtle Screen
t.bgcolor('white')
t.title("Naughty Face Drawing")
t.speed(0)


# define a function to draw a circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


# define a function to draw a straight line
def draw_line(color, width, x1, y1, x2, y2):
    t.penup()
    t.color(color)
    t.width(width)
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)


# draw the naughty face
draw_circle("red", 100, 0, -70)

# draw the eyes
draw_circle("white", 15, -30, 30)
draw_circle("white", 15, 30, 30)
draw_circle("black", 7, -30, 35)
draw_circle("black", 7, 30, 35)

# draw the nose
draw_circle("black", 10, 0, 10)

# draw the mouth
draw_line("black", 3, -20, -20, 20, -20)

# hide the turtle and display the drawing
t.hideturtle()
t.done()

