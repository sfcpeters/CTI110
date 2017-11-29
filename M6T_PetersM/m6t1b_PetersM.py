#CTI 110
#M6T1B_Initials
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

#drawing the letter M

speedy.hideturtle()     #hiding the turtle when the pen is up
speedy.penup()
speedy.left(180)
speedy.forward(300)
speedy.pendown()
speedy.showturtle()     #showing the turtle when the pen is down
speedy.right(90)
speedy.forward(200)
speedy.right(135)
speedy.forward(100)
speedy.left(90)
speedy.forward(100)
speedy.right(135)
speedy.forward(200)


#placing a space between letters

speedy.hideturtle()   #hiding the turtle when the pen is up
speedy.penup()
speedy.left(90)
speedy.forward(100)
speedy.pendown()
speedy.showturtle()   #showing the turtle when the pen is down

# drawing the letter E

speedy.left(90)
speedy.forward(200)
speedy.right(90)
speedy.forward(100)
speedy.hideturtle() #hiding the turtle when the pen is up
speedy.penup()
speedy.right(90)
speedy.forward(100)
speedy.right(90)
speedy.forward(50)
speedy.pendown()
speedy.showturtle()  #showing the turtle when the pen is down
speedy.forward(50)
speedy.hideturtle() #hiding the turtle when the pen is up
speedy.penup()
speedy.left(90)
speedy.forward(100)
speedy.left(90)
speedy.pendown()
speedy.showturtle()   #showing the turtle when the pen is down
speedy.forward(100)

#placing a space between letters

speedy.hideturtle()     #hiding the turtle when the pen is up
speedy.penup()
speedy.forward(100)
speedy.pendown()
speedy.showturtle()    #showing the turtle when the pen is down


# drawing the letter P

speedy.left(90)
speedy.forward(200)
speedy.right(90)
speedy.forward(100)
speedy.right(90)
speedy.forward(100)
speedy.right(90)
speedy.forward(100)
speedy.hideturtle() #hiding the turtle when the pen is up

win.exitonclick()
