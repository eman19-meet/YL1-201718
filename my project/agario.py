import time
import random
import turtle 
from ball import Ball

#turtle.tracer(0)
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
	x=random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS , int(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
	y=random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS , int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	while dx == 0 and dy == 0 :
		dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
		dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	radius=random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color=(random.random(),random.random(), random.random())

	new_ball=Ball(x,y,dx,dy,radius,color)
	BALLS.append(new_ball)

#PART 1 : MOVE ALL BALLS

def move_all_balls():
	for i in range (BALLS):
		new_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

#PART 2: CHECK FOR BALL COLLISION

def collide(ball_a, ball_b):
	if ball_a.r == ball_b.r and ball_a.pos() == ball_b.pos():
		return False
	D = math.sqrt(math.pow((ball_b.pos()[0]-ball_a.pos()[0]),2) + math.pow((ball_b.pos()[1]-ball_a.pos()[1],2)))
	if ball_a.r + ball_b.r >= D:
		return True
	else:
		return False

#PART 3 : CHECK COLLISIONS FOR ALL BALLS

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b) == True:
				a_radius = ball_a.r
				b_radius = ball_b.r
	X_COORDINATE = 	random.randint(round(-SCREEN_WIDTH) , round(SCREEN_WIDTH))
	Y_COORDINATE = 	random.randint(round(-SCREEN_HEIGHT) , round(SCREEN_HEIGHT))
	X_AXISSPEED = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	Y_AXISSPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	while X_AXISSPEED and Y_AXISSPEED == 0 :
		X_AXISSPEED = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
		Y_AXISSPEED = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	RADIUS = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	Color = (random.random(), random.random(),random.random())

	if ball_a.r > ball_b.r :
		ball_b.r = RADIUS
		ball_b.x = X_COORDINATE
		ball_b.y = Y_COORDINATE
		ball_b.dx = X_AXISSPEED
		ball_b.dy = Y_AXISSPEED
		ball_b.color(Color)
		ball_b.shapesize(ball_b.r/10)
		balla.r = ball_a.r+1
		ball_a.shapesize(ball_a.r/10)
	else:
		ball_a.r = RADIUS
		ball_a.x = X_COORDINATE
		ball_a.y = Y_COORDINATE
		ball_a.dx = X_AXISSPEED
		ball_a.dy = Y_AXISSPEED
		ball_a.color(Color)
		ball_a.shapesize(ball_a.r/10)
		ball_b.r = ball_b.r+1
		ball_b.shapesize(ball_b.r/10)

#PART 4 : CHECK COLLISION WITH MY BALL

def check_myball_collision():
	for i in range(BALLS):
		if collide(MY_BALL,BALLS[i]) == True:
			ball_radius = BALLS[i].r
			my_ball_radius = MY_BALL.r
			if MY_BALL.r < BALLS[i]:
				return False
			else:
				BALLS[i] = RADIUS
				BALLS[i].x = X_COORDINATE
				BALLS[i].y = Y_COORDINATE
				BALLS[i].dx = X_AXISSPEED
				BALLS[i].dy = Y_AXISSPEED
				BALLS[i].color(Color)
				BALLS[i].shapesize(ball_a.r/10)
				MY_BALL.r = ball_b.r+1
				MY_BALL.shapesize(ball_b.r/10)
		return True

#PART 5 : MOVEAROUND

def movearound(event):
	MY_BALL.goto( event.x-round(SCREEN_WIDTH) , round(SCREEN_HEIGHT)-event.y )

#PART 5.1 : MOVE IT!
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

#PART 6 : THE WHILE LOOP 
