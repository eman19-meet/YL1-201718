import time
import random
import turtle 
import math
from ball import Ball

turtle.tracer(0)
turtle.hideturtle()
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

#PART 0 : CREATING THE BALLS

MY_BALL=Ball(100,100,3,3,10,"blue")
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-2
MINIMUM_BALL_DY=-2
MAXIMUM_BALL_DY=2
MAXIMUM_BALL_DX=2

BALLS=[]

for i in range(NUMBER_OF_BALLS):
	x=random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS , int(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
	y=random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS , int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	while dx == 0 or dy == 0 :
		dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
		dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	radius=random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color=(random.random(),random.random(), random.random())

	new_ball=Ball(x,y,dx,dy,radius,color)
	BALLS.append(new_ball)

#PART 1 : MOVE ALL BALLS

def move_all_balls():
	for new_ball in BALLS:
		new_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

#PART 2: CHECK FOR BALL COLLISION

def collide(ball_a, ball_b):
	if ball_a.r == ball_b.r and ball_a.pos() == ball_b.pos():
		return False
	D = math.sqrt(math.pow((ball_b.pos()[0]-ball_a.pos()[0]),2) + math.pow((ball_b.pos()[1]-ball_a.pos()[1]),2))
	if ball_a.r + ball_b.r >= D + 10:
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
				x=random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS , int(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
				y=random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS , int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
				dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				while dx == 0 or dy == 0 :
					dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
					dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				RADIUS = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				Color = (random.random(), random.random(),random.random())

				if ball_a.r > ball_b.r :
					ball_b.goto(x,y)
					ball_b.r = RADIUS
					ball_b.x = x
					ball_b.y = y
					ball_b.dx = dx
					ball_b.dy = dy
					ball_b.color(Color)
					ball_b.shapesize(ball_b.r/10)
					ball_a.r = ball_a.r+1
					ball_a.shapesize(ball_a.r/10)
				else:
					ball_a.goto(x,y)
					ball_a.r = RADIUS
					ball_a.x = x
					ball_a.y = y
					ball_a.dx = dx
					ball_a.dy = dy
					ball_a.color(Color)
					ball_a.shapesize(ball_a.r/10)
					ball_b.r = ball_b.r+1
					ball_b.shapesize(ball_b.r/10)

#PART 4 : CHECK COLLISION WITH MY BALL

def check_myball_collision():
	for i in range(len(BALLS)):
		if collide(MY_BALL,BALLS[i]) == True:
			ball_radius = BALLS[i].r
			my_ball_radius = MY_BALL.r
			if MY_BALL.r < ball_radius:
				return False
			else:
				x=random.randint(int(-SCREEN_WIDTH) + MAXIMUM_BALL_RADIUS , int(SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
				y=random.randint(int(-SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS , int(SCREEN_HEIGHT) - MAXIMUM_BALL_RADIUS)
				dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				while dx or dy == 0 :
					dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
					dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				RADIUS = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				Color = (random.random(), random.random(),random.random())
				BALLS[i].r = RADIUS
				BALLS[i].x = x
				BALLS[i].y = y
				BALLS[i].dx = dx
				BALLS[i].dy = dy
				BALLS[i].color(Color)
				BALLS[i].shapesize(BALLS[i].r/10)
				MY_BALL.r = MY_BALL.r+1
				MY_BALL.shapesize(MY_BALL.r/10)
	return True

#PART 5 : MOVEAROUND

def movearound(event):
	MY_BALL.goto( event.x-round(SCREEN_WIDTH) , round(SCREEN_HEIGHT)-event.y )

#PART 5.1 : MOVE IT!
turtle.getcanvas().bind("<Motion>", movearound)
turtle.getscreen().listen()

#PART 6 : THE WHILE LOOP 
while RUNNING == True:
	if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
		SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
		SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
	move_all_balls()
	check_all_balls_collision()
	# move(SCREEN_WIDTH,SCREEN_HEIGHT)
	RUNNING = check_myball_collision()
	turtle.getscreen().update()
	time.sleep(SLEEP)