import turtle

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
