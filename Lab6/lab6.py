from turtle import *
import random
import math

class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(raduis)
		self.color(color)
		self.speed(speed)


b1=Ball('raduis':7,'color':"red",'speed':20)
b2=Ball('raduis':10,'color':"blue",'speed':50)

def check_collision(ball1,ball2):
		if math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+math.pow((ball1.ycor()-ball2.ycor()),2)) <= (ball1.radius()+ball2.raduis()):
			print("the 2 balls collision")
			ball1.color("green")
			ball2.color("yellow")
		else :
			print("the 2 balls dont collision")


