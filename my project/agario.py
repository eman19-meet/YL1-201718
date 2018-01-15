import time
import random
from ball import Ball

turtle.tracer(0)
turtle.hideturtle()
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

#PART 0 : CREATING THE BALLS

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
	while dx == 0 and dy == 0 :
		dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
		dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	radius=random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color=random.randint(random.random(),random.randint())

	new_ball=Ball(x,y,dx,dy,radius,color)
	MY_BALL.append(new_ball)

#PART 1 : MOVE ALL BALLS

def move_all_balls():
	for i in range (BALLS):
		new_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

#PART 2: CHECK FOR BALL COLLISION

def collide(ball_a, ball_b):
	if ball_a.r == ball_b.r and ball_a.pos() == ball_b.pos()
		return False
	D = math.sqrt(math.pow((ball_b.pos()[0]-ball_a.pos()[0]),2) + math.pow((ball_b.pos()[1]-ball_a.pos()[1],2))
		#I finished till the distance of the 2 balls but I dont think its 100% right