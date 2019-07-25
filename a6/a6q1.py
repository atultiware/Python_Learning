class Demo:
	value = 0
	
	def __init__(self, no1, no2):	
		self.n1 = no1
		self.n2 = no2
	
	def Fun(self):	
		print(self.n1)
		print(self.n2)
		
	def Gun(self):	
		print(self.n1)
		print(self.n2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)


obj1.Fun()
obj2.Fun()

obj1.Gun()
obj2.Gun()
