'''
Created on 24 Jul 2020

@author: Lilian
'''

import turtle
import math

from matplotlib.pyplot import draw
my_turtle = turtle.Turtle()
my_turtle.showturtle()

####################      WRITE YOUR CODE BELOW      #########################
yval = 0

def draw_triangle(length):
    my_turtle.right(60)
    my_turtle.pendown()
    for i in range(3):
        my_turtle.forward(length)
        my_turtle.right(120)
    my_turtle.penup()
    my_turtle.left(60)



lengths = [x for x in range(250, 0, -25)]

for length in lengths:
    yval -= 15
    draw_triangle(length)
    my_turtle.sety(yval)


#################### WRITE YOUR CODE ABOVE THIS LINE #########################
####################        IGNORE CODE BELOW        #########################

## Must be the last line of code 
my_turtle.screen.exitonclick()
