import turtle
import random
colormode(255)

#exercise 1:
class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesie(size)
		self.shape("square")
#exercise 1 extra 1:
	def Random_color(self):
		Turtle.__init__(self)
		random.randint(0,256)
		r=random.randint(0,256)
		g=random.randint(0,256)
		b=random.randit(0,256)
		self.color(r,g,b)

square1=square(20)
square1.Random_color()

#exercise 1 extra 2:
class Rectangle(Turtle):
	def __init__(self,width,height):
		self.shapeweidth(width)
		self.shapeheight(height)
	
	def Rectangle_shape(self):
		Turtle.__init__(self)
		for i in range(2):
			self.forward(self.shapewidth)
			self.right(90)
			self.forward(self.shapeheight)
			self.right(90)
r1=Rectangle(20,5)
r1.Rectangle_shape()

#exercise 2:
class Hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		#its wrong!!!!!!
		for i in range(6):
			self.forward(80)
			self.right(60)









	

