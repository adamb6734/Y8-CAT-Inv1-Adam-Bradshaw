#fractal trees
import random

def startriangle(n):
    if n > 0:
        print("*" * n)
        startriangle(n-1)
#task4
#startriangle(5)

def triangular(n):
    if n == 0:
        return 0
    else:
        return n + triangular(n-1)
#task5
#print(triangular(9))

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

#Create Screen
screen = turtle.Screen()
screen.bgcolor("White")

#Create turtle object
pen = turtle.Turtle()
pen.color("Brown")
pen.speed(0)

#Move starting position to bottom of screen
pen.penup()
pen.goto(0, -200)
pen.pendown()

#Face turtle upwards
pen.left(90)

#Recursive function: draws a branch, then calls itself to draw smaller branches
def fractaltree(n, length, angle, scale):
    if n == 0:
        pen.dot(6, "green") #draw small green circle at the end of branches to appear as leaves
        return #Base case: stop recursion

    #Draw main branch
    pen.forward(length)

    #Save current position and direction
    pos = pen.position()
    direction = pen.heading()

    #Draw left branch
    pen.left(angle)
    fractaltree(n-1, length*scale, angle, scale)

    #Return to saved position
    pen.penup()
    pen.goto(pos)
    pen.setheading(direction)
    pen.pendown()

    #draw right branch
    pen.right(angle)
    fractaltree(n-1, length*scale, angle, scale)

    #return again to original position
    pen.penup()
    pen.goto(pos)
    pen.setheading(direction)
    pen.pendown()

# Task 10: new function to later include randomness
# currently same as fractaltree (will modify with randomness)
def randomfractaltree(n, length, angle, scale):
    if n == 0:
        pen.dot(6, "green")  # draw small green circle at the end of branches to appear as leaves
        return #Base case: stop recursion

    #Draw main branch
    pen.forward(length)

    #Save current position and direction
    pos = pen.position()
    direction = pen.heading()

    #Randomness section for gamblers
    angle_variation = random.randint(-10, 10)
    scale_variation = random.uniform(0.9, 1.1)


    # Draw left branch
    pen.left(angle + angle_variation)
    randomfractaltree(n-1, length*scale*scale_variation, angle, scale)

    #Return to saved position
    pen.penup()
    pen.goto(pos)
    pen.setheading(direction)
    pen.pendown()

    #draw right branch
    pen.right(angle + angle_variation)
    randomfractaltree(n-1, length*scale*scale_variation, angle, scale)

    #return again to original position
    pen.penup()
    pen.goto(pos)
    pen.setheading(direction)
    pen.pendown()


#User input (menu system for Task 9)
print("Fractal Tree Generator")
print("Recommended input: (8,100,30,0.75)")

# Get inputs (strings first)
n = turtle.textinput("Level", "Enter tree level:")
length = turtle.textinput("Length", "Enter branch length:")
angle = turtle.textinput("Angle", "Enter angle between adjacent branches:")
scale_input = turtle.textinput("Scale", "Enter branch length scale (e.g. 0.75):")

# Convert to correct types
n = int(n)
length = int(length)
angle = int(angle)

# Handle scale safely (optional input)
if scale_input is None or scale_input == "":
    scale = 0.75  # default value
else:
    scale = float(scale_input)


randomfractaltree(n, length, angle, scale)

#Hides the turtle when everything is drawn
pen.hideturtle()

#keep window open
turtle.done()


