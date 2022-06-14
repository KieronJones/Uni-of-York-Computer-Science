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
def draw_polygon(sides):
    rotation = (360/sides)
    my_turtle.pendown()
    for i in range(sides):
        my_turtle.forward(100)
        my_turtle.right(rotation)
    my_turtle.penup()


draw_polygon()



#################### WRITE YOUR CODE ABOVE THIS LINE #########################
####################        IGNORE CODE BELOW        #########################

## Must be the last line of code 
my_turtle.screen.exitonclick()
