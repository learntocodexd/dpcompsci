import turtle

def tree(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(3):
        t.down()
        t.left(120)
        t.forward(100)
    t.end_fill()
    t.up()
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

def apple(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(1):
        t.down()
        t.circle(10)
    t.end_fill()
    t.up()
    
t = turtle.Turtle()
t.up()
t.goto(200,100)
tree("green")
t.goto(175,100)
trunk("brown")
t.goto(175,110)
apple("red")
t.goto(150,140)
apple("red")
t.goto(125,110)
apple("red")
hideturtle()
