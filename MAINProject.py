import turtle
from FunctionFileProject import*
bob = turtle.Turtle()
turtle.bgcolor("black")
turtle.colormode(255)

bob.speed(11)

for times in range(50):
    bob.color("blue")
    bob.forward(100)
    bob.right(20)
    bob.forward(20)
    bob.left(50)
    bob.forward(50)
    bob.right(20)
    
    bob.penup()
    bob.setposition(0, 0)
    bob.pendown()
    
    bob.right(2)

for times in range(90):
    bob.color(times*2,times*2,times*2)
    bob.begin_fill()
    bob.circle(times)
    bob.forward(times*1.5)
    bob.left(10)
    bob.end_fill()

bob.penup()
bob.setposition(0,0)
bob.pendown()
bob.right(10)

for times in range(80):
    bob.color(times*2,times*2,times*2)
    bob.begin_fill()
    bob.circle(times)
    bob.forward(times*2)
    bob.left(10)
    bob.end_fill()

bob.penup()
bob.setposition(0,0)
bob.pendown()
bob.right(25)

for times in range(80):
    bob.color(times*2,times*2,times*2)
    bob.begin_fill()
    bob.circle(times)
    bob.forward(times*2.5)
    bob.left(10)
    bob.end_fill()

bob.penup()
bob.setposition(0,0)
bob.pendown()
bob.right(4)

for times in range(80):
    bob.color(times*2,times*2,times*2)
    bob.begin_fill()
    bob.circle(times)
    bob.forward(times*3)
    bob.left(10)
    bob.end_fill()

bob.penup()
bob.setposition(0,0)
bob.pendown()
bob.right(5)

for times in range(80):
    bob.color(times*2,times*2,times*2)
    bob.begin_fill()
    bob.circle(times)
    bob.forward(times*3.5)
    bob.left(10)
    bob.end_fill()

bob.penup()
bob.setposition(0,0)
bob.pendown()
bob.right(10)

for times in range(80):
    bob.color(times*2,times*2,times*2)
    bob.begin_fill()
    bob.circle(times)
    bob.forward(times*4)
    bob.left(10)
    bob.end_fill()

bob.penup()
bob.setposition(0,0)
bob.pendown()
bob.right(15)

for times in range(80):
    bob.color(times*2,times*2,times*2)
    bob.begin_fill()
    bob.circle(times)
    bob.forward(times*4.5)
    bob.left(10)
    bob.end_fill()

bob.penup()
bob.setposition(0,0)
bob.pendown()
bob.right(20)

for times in range(80):
    bob.color(times*2,times*2,times*2)
    bob.begin_fill()
    bob.circle(times)
    bob.forward(times*5)
    bob.left(10)
    bob.end_fill()
    
turtle.done()
