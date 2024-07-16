# Draw babaji emoji
import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Smiley Face")

# Create a Turtle object
smiley = turtle.Turtle()
smiley.pensize(30)
smiley.speed(0.5)  # Set the drawing speed


# Function to draw a filled circle
def filled_circle(color, radius):
    smiley.penup()
    smiley.fillcolor(color)
    smiley.begin_fill()
    smiley.circle(radius)
    smiley.end_fill()


# Function to draw an arc for the smile
def draw_smile():
    smiley.penup()
    smiley.goto(50, 50)
    smiley.pendown()
    smiley.setheading(90)
    smiley.circle(50, 180)


# Draw the smiley face
filled_circle("red", 100)

# Draw the eyes
smiley.penup()
smiley.goto(-40, 120)
smiley.pendown()
filled_circle("white", 15)

smiley.penup()
smiley.goto(40, 120)
smiley.pendown()
filled_circle("white", 15)

# Draw the pupils
smiley.penup()
smiley.goto(-37, 130)
smiley.pendown()
filled_circle("black", 9)

smiley.penup()
smiley.goto(37, 130)
smiley.pendown()
filled_circle("black", 9)

# Draw the smile
draw_smile()

# Hide the Turtle
smiley.hideturtle()

# Close the window when clicked
screen.exitonclick()
