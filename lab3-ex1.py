import turtle
import random
#lab 3 exercise 1:

#turtle.penup()
#turtle.goto(0,60)
#turtle.pendown()
#turtle.color("red")
#turtle.goto(60,60)
#turtle.color("blue")
#turtle.goto(0,0)
#turtle.color("yellow")
#turtle.goto(30,90)
#turtle.color("green")
#turtle.goto(60,0)
#turtle.color("black")
#turtle.goto(0,60)

turtle.penup()
turtle.goto(50,50)
turtle.pendown()
a=["blue","red","yellow","orange","pink"]
for i in range(2):
    turtle.color(random.choice(a))
    turtle.forward(100)
    turtle.right(150)
    turtle.color(random.choice(a))
    turtle.forward(100)
    turtle.right(150)
    turtle.color(random.choice(a))
turtle.goto(50,50)
