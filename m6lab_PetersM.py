#CTI 110
#M6T1C_Initials
#Michael Peters
#27 November 2017


import turtle


wn = turtle.Screen()
speedy = turtle.Turtle()

# add some display options
speedy.shape("turtle")
speedy.pensize(6)               # increase or decrease pensize (takes integer)
speedy.pencolor("black")          # set pencolor (takes string)
speedy.fillcolor("green")       # set speedy's fillcolor (takes string)
speedy.speed(5)                 # increase or decrese speed (takes integer)


for i in range (1,6):
    speedy.penup()
    speedy.forward(150)
    speedy.left(45)
    speedy.forward(75)
    speedy.right(45)
    speedy.pendown()



    speedy.forward(40)
    speedy.backward(40)
    speedy.left(90)
                            
    speedy.forward(40)
    speedy.backward(40)
    speedy.right(45)
    speedy.backward(75)
    speedy.left(90)
            
    speedy.backward(75)
    speedy.left(135)
                
    speedy.forward(40)
    speedy.backward(40)
    speedy.left(90)
            
    speedy.forward(40)
    speedy.backward(40)
    speedy.left(135)
    speedy.forward(75)

    speedy.right(135)
    speedy.forward(75)

    
    speedy.left(45)
    speedy.forward(60)
    speedy.backward(60)
    speedy.right(90)
    speedy.forward(60)
    speedy.backward(60)
    speedy.left(45)

    
    speedy.backward(125)

    speedy.left(45)
    speedy.forward(60)
    speedy.right(45)
    speedy.forward(32.5)
    speedy.backward(32.5)
    speedy.left(90)
                            
    speedy.forward(32.5)
    speedy.backward(32.5)
    speedy.right(45)
    speedy.backward(60)
    speedy.left(90)
            
    speedy.backward(60)
    speedy.left(135)
                
    speedy.forward(32.5)
    speedy.backward(32.5)
    speedy.left(90)
            
    speedy.forward(32.5)
    speedy.backward(32.5)
    speedy.left(135)
    speedy.forward(60)

    speedy.right(135)
    speedy.backward(50)
    speedy.left(45)
    speedy.forward(45)
    speedy.right(45)
    speedy.forward(25)
    speedy.backward(25)
    speedy.left(90)
                            
    speedy.forward(25)
    speedy.backward(25)
    speedy.right(45)
    speedy.backward(45)
    speedy.left(90)
            
    speedy.backward(45)
    speedy.left(135)
                
    speedy.forward(25)
    speedy.backward(25)
    speedy.left(90)
            
    speedy.forward(25)
    speedy.backward(25)
    speedy.left(135)
    speedy.forward(45)

    speedy.right(135)
    speedy.backward(50)
    speedy.left(72)

wn.exitonclick()
