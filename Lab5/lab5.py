import turtle
import random

class Square(turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesie(size)
		self.shape("square")

	def Random_color(self):
		random.randint(0,256)
		r=random.randint(0,256)
		g=random.randint(0,256)
		b=random.randit(0,256)
		self.color(r,g,b)

square1=square(20)
square1.Random_color()



