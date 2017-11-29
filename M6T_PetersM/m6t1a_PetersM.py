#CTI 110
#M6T1A_Shapes
#Michael Peters
#27 November 2017

import turtle
win = turtle.Screen()
speedy = turtle.Turtle()

# add some display options
speedy.shape("turtle")
speedy.pensize(6)               # increase or decrease pensize (takes integer)
speedy.pencolor("black")          # set pencolor (takes string)
speedy.fillcolor("orange")       # set speedy's fillcolor (takes string)
speedy.speed(1)                 # increase or decrese speed (takes integer)

#drawing square

for x in range(4):

    speedy.forward(100)
    speedy.left(90)
    

#placing a space between shapes

speedy.hideturtle()     #hiding the turtle when the pen is up    
speedy.penup()
speedy.right(90)
speedy.forward(100)
speedy.left(90)
speedy.forward(50)
speedy.pendown()
speedy.showturtle()    #showing the turtle when the pen is down

# drawing triangle

speedy.right(60)
speedy.forward(100)
speedy.right(120)
speedy.forward(100)
speedy.right(120)
speedy.forward(100)



win.exitonclick()
