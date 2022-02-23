class Basic:
	def __init__(self,name):
		self.name = name
	def intro(self):
		print("welcome to the hackers world-->",self.name)

class Chaaa(Basic):
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def welcome(self):
		print(f"hii {self.name}, welcome to the hacker word")
		print(f"your age is {self.age}")

d = Chaaa("bhadri",19)
d.welcome()
d.intro()