class Animal(object):
	def __init__ (self,sound,name,age,favorite_color):
		self.sound=sound
		self.name=name
		self.age=age
		self.favorate_color=favorite_color

	def eat(self,food):
		print("Yummy!! "+self.name+" is eating "+food)

	def description(self):
		print(self.name+" is "+self.age+" years old, and loves the collor "+self.favorate_color)

	def make_sound(self):
		print(self.sound *3)

	def sound_X(self,x):
		print(self.sound *x)

a = Animal("haha","cat", 4, "yellow")
a.eat("meat")
a.make_sound()
a.sound_X(17)
a.description()

class Person(object):	
	def __init__ (self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender

	def favorate_breakfast(self,breakfast):
		print(self.name + " is eating his favorate breakfast , which is : " + breakfast)

	def favorate_sport(self,sport):
		print(sport + " is " + self.name +"'s favorate sport!!!")

p = Person("eman",15,"kfar kanna", "female")
p.favorate_breakfast("milk")
p.favorate_sport("football")

class Song(object):
	def __init__ (self,[]lyrics):
		self.lyrics=lyrics

	def sing_me_a_song(self):
		for i in lyrics:
			print(lyrics[i])

flower_song=Song(["Roses are red," , 
	"Violets are blue," ,
	 "I wrote this poem for you."])

flower_song.sing_me_a_song()