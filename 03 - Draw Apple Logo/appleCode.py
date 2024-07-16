
import turtle

t = turtle.Turtle()
t.speed(20)
t.pensize(1)
t.pencolor("black")

def curve1():
 for i in range(90):
t.left(1)
t.forward(1)

def curve2():
 for i in range(90):
 t.right(1)
 t.forward(1)

def curve3():
 curve1()
 t.forward(80)
 curve1()

def curve4():
 curve1()
 t.forward(90)
 curve1()

def half():
 t.forward(50)
 curve1()
 t.forward(90)
 curve3()
 t.forward(40)
 t.left(90)
 t.forward(80)
 t.right(90)
 t.forward(10)
 t.right(90)
 t.forward(120) 
 t.curve4()
 t.forward(30)
 t.left(90)
 t.forward(50)
 curve2()
 t.forward(40)
 t.end_fill()

def pos():
 t.penup()
 t.forward(20)
 t.right(90)
 t.forward(10)
 t.right(90)
 t.pendown()

def dot():
 t.penup()
 t.right(90)
 t.forward(160)
 t.left(90)
 t.forward(70)
 t.pencolor("black")
 t.dot(35)

def dot2():
 t.left(90)
 t.penup()
 t.forward(310)
 t.left(90)
 t.forward(120)
 t.pendown()

t.dot(35)

t.fillcolor("#306998")
t.begin_fill()
half()
t.end_fill()
pos()
t.fillcolor("#FFD43B")
t.begin_fill()
half()
t.end_fill()

dot()
dot2()

def pause():
t.speed(2)
 for i in range(100):
t.left(90)
pause()
