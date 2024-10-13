class perceptron():
	def __init__(self):
		self.w1=self.w2=1
		self.x1=int(input("x1: "))
		self.x2=int(input("x2: "))
		self.b =int(input("b1: "))

	def output(self):
		if self.w1*self.x1+self.w2*self.x2+self.b > 0	: return 1
		else											: return 0

p1=perceptron()
print(p1.output())
