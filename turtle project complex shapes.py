'''
Project Name: Turtles Pattern II
Author: Dustin Parker
Due Date: 04/09/2021
Course: CS1400-005

This project codes to creat a scene using the turtles program. It creates a forest with apples in the
trees as well as coding for a Sun in the sky. It includes a green grass ground, and a blue sky.
I used a randomizer so that the trees will be in a different spot everytime within it's parameters.'''


import turtle

import math

import sys

import random

def main():
    
    #this is for the user to input their own personal width and height for the window and allowing
    #the program to properly function within thonny and command window
    if len(sys.argv) == 1:
        width = input("Enter the turtle window width: ")
        height = input("Enter the turtle window height: ")
       
    else:
        if len(sys.argv) != 3:
            print("Not enough or too many arguements.")
            return
    
        width = (sys.argv[1])
        height = (sys.argv[2])
    try:
        width = float(width)
        height = float(height)
    except ValueError:
        print("Enter postive integers for width and height.")
        return
    #this is to prevent users from entering negative integers for the width/height of the window
    if width < 1 or height < 1:
        print("Enter postive integers for width and height.")
        return
    def rectangle(color, width, height):
        t.begin_fill()
        t.fillcolor(color)
        for i in range(2):
            t.down()
            t.right(90)
            t.forward(height)
            t.right(90)
            t.forward(width)
        t.end_fill()
        t.up()
    #this is the function to create the triangle top for the tree
    def tree(width, height, scale):
        t.begin_fill()
        t.fillcolor("green")
        for i in range(3):
            t.down()
            t.left(120)
            t.forward(100 * scale)
        t.end_fill()
        t.up 
    #this is the function to create the rectangle for the tree trunk
        t.begin_fill()
        t.fillcolor("brown")
        for i in range(1):
            t.right(180)
            t.forward(75 * scale)
            t.down()
            t.left(90)
            t.forward(100 * scale)
            t.left(90)
            t.forward(50 * scale)
            t.left(90)
            t.forward(100 * scale)
        t.end_fill()
    #this is the function to create the circles for the apple
        t.begin_fill()
        t.fillcolor("red")
        for i in range(1):
            t.up()
            t.forward(15 * scale)
            t.down()
            t.circle(10 * scale)
        t.end_fill()
    #this is for the apple with a larger radius
        t.begin_fill()
        t.fillcolor("red")
        for i in range(1):
            t.up()
            t.left(20)
            t.forward(40 * scale)
            t.down()
            t.circle(15 * scale)
        t.end_fill()
        t.up()
        t.setheading(0)
        t.up()
        
    
        
        #this is used for the function of sun in the picture
    def sun(x,y,scale):
        width = 200 * scale
        height = 25 * scale
        
        #this is the sun rays
        radius= 50*scale
        t.begin_fill()
        t.fillcolor("yellow")
        t.goto(x - (height/2),y + radius + (width/2))
        t.setheading(90)
        for i in range(2):
            t.down()
            t.right(90)
            t.forward(height)
            t.right(90)
            t.forward(width)
        t.end_fill()
        t.up()
        t.setheading(0)
        t.goto(x+(200 * scale/2),y+radius+(25 * scale/2))
        t.begin_fill()
        for i in range(2):
            t.down()
            t.right(90)
            t.forward(25 * scale)
            t.right(90)
            t.forward(200 * scale)
        t.end_fill()
        #this codes for the circle of the sun
        t.up()
        t.goto(x,y)
        t.down()
        t.begin_fill()
        t.fillcolor("yellow")
        for i in range(1):
            t.down()
            t.circle(radius)
        t.end_fill()
        t.up()
        
        
        
    #this is the code that contains the coordinates as well as the color for each function to use, the scale
        # and the randomized trees
    t = turtle.Turtle()
    t.screen.setup(width,height)
    t.speed(0)
    t.up()
    t.goto(2500,0)
    rectangle("green", 5000, 1000)
    t.goto(2500,1000)
    rectangle("blue", 5000, 1000)
    for i in range(10):
        x= random.randint(-400,400)
        y= random.randint(-400,0)
        t.goto(x,y)
        tree(100,200, 1)
    sun(-300,400, 1)
    sun(200,400,.5)
    t.hideturtle()


if __name__ == "__main__":
    main()
    
