#fractal trees

def startriangle(n):
    if n > 0:
        print("*" * n)
        startriangle(n-1)
#task4
# startriangle(5)

def triangular(n):
    if n == 0:
        return 0
    else:
        return n + triangular(n-1)
#task5
#print(triangular(6))

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
#task6
#print(fibonacci(10))

#import turtle
#create turtle screen and set background colour
#screen=turtle.Screen()
#screen.bgcolor("White")
# create a turtle object to draw with
#pen=turtle.Turtle()
# set colour of the turtle
#pen.color("Blue")
# set speed of the turtle
#pen.speed(2)
# draw line of length 20 pixels
#pen.forward(20)
# rotate the turtle 90 degrees to the right to
# change the direction it’s about to draw in
#pen.right(90)
# draw the other 3 sides of a rectangle
#pen.forward(40)
#pen.right(90)
#pen.forward(20)
#pen.right(90)
#pen.forward(40)
#hide turtle
#pen.hideturtle()
#keep turtle window open when done
#turtle.done()

import turtle

screen = turtle.Screen()
screen.bgcolor("White")

pen = turtle.Turtle()
pen.color("Brown")
pen.speed(0)
pen.penup()
pen.goto(0, -200)
pen.pendown()

pen.left(90)

def simpletree(n, length):
    if n == 0:
        return

    pen.forward(length)

    pos = pen.position()
    dir = pen.heading()
    pen.left(30)
    simpletree(n-1, length * 0.7)

    pen.penup()
    pen.goto(pos)
    pen.setheading(dir)
    pen.pendown()

    pen.right(30)
    simpletree(n-1, length * 0.7)

    pen.penup()
    pen.goto(pos)
    pen.setheading(dir)
    pen.pendown()

simpletree(8, 80)

turtle.done()