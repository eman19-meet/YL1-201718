import turtle
import time
import random
from ball.py import Ball

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.penup()
		self.setpos(x,y)
		self.dx=dx
		self.dy=dy
		self.r=r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)
	def move(self,screen_width,screen_height):
		self.current_x=self.xcor()
		self.new_x=self.current_x+dx
		self.current_y=self.ycor()
		self.new_y=self.current_y+dy
		self.right_side_ball=new_x+r
		self.left_side_ball=new_x-r
		self.up_side_ball=new_y+r
		self.down_side_ball=new_y-r
		self.goto(new_x,new_y)
		if right_side_ball > -screen_width/2:
			self.goto(new_x - self.dx , new_y)
		if left_side_ball < -screen_width/2:
			self.goto(new_x + self.dx , new_y)
		if up_side_ball > -screen_height/2:
			self.goto(new_x , new_y - self.dy)
		if down_side_ball < -screen_height/2:
			self.goto(new_x , new_y + self.dy)

turtle.tracer(0)
turtle.hideturtle()
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(0,0,3,3,10,"blue")
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5
MAXIMUM_BALL_DX=5

BALLS=[]

for i in range(NUMBER_OF_BALLS):
	x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	radius=random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color=random.randint(random.random(),random.randint())
