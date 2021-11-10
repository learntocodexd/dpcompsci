'''
Project Name: Turtles Pattern 
Author: Dustin Parker
Due Date: 02/20/2021
Course: CS1400-005


This code is to create a tree with a green triangle as the branches, brown rectangle as the trunk, and red
circle as the apples. There is also a small puddle on the ground near the tree.
This also adds a function that allows the user to add their own unique width and height of the turtle window.
I learned how to use shapes and coordinates in turtle. I gained a better understanding of functions and how
to implement them into my code alongside loops. I reccommend that the window and height should be 800x800
'''

import turtle


def main():
    
    
    #this is for the user to input their own personal width and height for the window
    try:
        width = float(input("Enter the turtle window width: "))
        height = float(input("Enter the turtle window height: "))
    except ValueError:
        print("Enter postive integers for width and height.")
        return
    
    
    #this is to prevent users from entering negative integers for the width/height of the window
    if width < 1 or height < 1:
        print("Enter postive integers for width and height.")
        return
    
    
    #this is the function to create the triangle top for the tree
    def tree(color):
        t.begin_fill()
        t.fillcolor(color)
        for i in range(3):
            t.down()
            t.left(120)
            t.forward(100)
        t.end_fill()
        t.up()

    
    #this is the function to create the rectangle for the tree trunk
    def trunk(color):
        t.begin_fill()
        t.fillcolor(color)
        for i in range(2):
            t.down()
            t.right(90)
            t.forward(100)
            t.right(90)
            t.forward(50)
        t.end_fill()
        t.up()
    
    
    #this is the function to create the circles for the apple
    def apple(color):
        t.begin_fill()
        t.fillcolor(color)
        for i in range(1):
            t.down()
            t.circle(10)
        t.end_fill()
        t.up()

    def apple15(color):
        t.begin_fill()
        t.fillcolor(color)
        for i in range(1):
            t.down()
            t.circle(15)
        t.end_fill()
        t.up()
        
    #this is the code that contains the coordinates as well as the color for each function to use
    t = turtle.Turtle()
    t.screen.setup(width,height)
    t.up()
    t.goto(200,100)
    tree("green")
    t.goto(175,100)
    trunk("brown")
    t.right(90)
    t.goto(0,-50)
    trunk("blue")
    t.goto(175,110)
    apple("red")
    t.goto(150,140)
    apple("red")
    t.goto(120,110)
    apple15("red")
    t.hideturtle()


if __name__ == "__main__":
    main()
    